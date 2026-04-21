#!/usr/bin/env python3
"""
extract_papers.py — 批量解析导师 PDF 论文，输出结构化文本 + 多维风格指标

用法:
    python3 extract_papers.py <pdf_dir_or_file> [--output <output_dir>]

输出:
    - <论文名>_text.txt       按章节结构化文本
    - <论文名>_parsed.json    机器可读结构化数据
    - _summary.json           跨论文汇总统计
    - _frequent_words.json    高频词汇 Top 50
    - _connector_words.json   连接词使用统计

依赖:
    pip install pymupdf
"""

import sys
import os
import re
import json
import argparse
from pathlib import Path
from collections import Counter

try:
    import fitz  # PyMuPDF
except ImportError:
    print("缺少依赖，请先运行: pip install pymupdf")
    sys.exit(1)


# ── 章节标题识别 ─────────────────────────────────────────────────────────
SECTION_KEYWORDS = [
    r"^abstract",
    r"^1[\.\s]+introduction",
    r"^2[\.\s]+",
    r"^3[\.\s]+",
    r"^4[\.\s]+",
    r"^5[\.\s]+",
    r"^related\s+work",
    r"^background",
    r"^method",
    r"^experiment",
    r"^result",
    r"^discussion",
    r"^conclusion",
    r"^reference",
    r"^acknowledge",
]
SECTION_RE = re.compile("|".join(SECTION_KEYWORDS), re.IGNORECASE)

# ── 停用词（学术英文常见） ──────────────────────────────────────────────
STOP_WORDS = {
    "the", "a", "an", "is", "are", "was", "were", "be", "been", "being",
    "have", "has", "had", "do", "does", "did", "will", "would", "could",
    "should", "may", "might", "shall", "can", "need", "dare", "ought",
    "to", "of", "in", "for", "on", "with", "at", "by", "from", "as",
    "into", "through", "during", "before", "after", "above", "below",
    "between", "out", "off", "over", "under", "again", "further",
    "then", "once", "here", "there", "when", "where", "why", "how",
    "all", "each", "every", "both", "few", "more", "most", "other",
    "some", "such", "no", "nor", "not", "only", "own", "same", "so",
    "than", "too", "very", "just", "because", "but", "and", "or",
    "if", "while", "that", "this", "these", "those", "it", "its",
    "we", "our", "us", "they", "their", "them", "which", "what",
    "also", "about", "up", "down", "however", "therefore", "thus",
    "moreover", "furthermore", "although", "using", "used", "based",
    "proposed", "show", "shown", "shows", "results", "result",
}

# ── 连接词分类 ─────────────────────────────────────────────────────────
CONNECTORS = {
    "递进": [
        "furthermore", "moreover", "in addition", "additionally",
        "besides", "also", "similarly", "likewise",
    ],
    "转折": [
        "however", "nevertheless", "nonetheless", "in contrast",
        "conversely", "on the other hand", "although", "while",
        "whereas", "despite", "yet", "but",
    ],
    "因果": [
        "therefore", "consequently", "as a result", "thus", "hence",
        "accordingly", "for this reason", "so",
    ],
    "总结": [
        "in summary", "to summarize", "overall", "in conclusion",
        "in brief", "to conclude", "finally", "in short",
    ],
    "举例": [
        "for example", "for instance", "specifically", "in particular",
        "namely", "such as", "e.g.", "i.e.",
    ],
}

# ── Hedging & Assertive 词汇 ───────────────────────────────────────────
HEDGE_WORDS = {
    "情态动词": ["may", "might", "could", "should"],
    "认知动词": ["suggest", "indicate", "appear", "seem", "tend to", "imply"],
    "程度副词": ["approximately", "generally", "typically", "relatively",
                 "potentially", "likely", "possibly", "roughly"],
}

ASSERTIVE_WORDS = {
    "证明类": ["demonstrate", "prove", "confirm", "establish", "validate"],
    "展示类": ["show", "reveal", "illustrate", "exhibit", "present"],
    "强调副词": ["significantly", "notably", "remarkably", "clearly",
                 "obviously", "substantially", "considerably"],
}


def extract_year_from_pdf(pdf_path: Path) -> str:
    """从 PDF 中提取发表年份，优先级：文件名 > 元数据 > 正文前3页"""
    # 策略 1：文件名中的 4 位数字（1900-2099）
    name_years = re.findall(r"\b(19\d{2}|20\d{2})\b", pdf_path.stem)
    if name_years:
        return name_years[-1]  # 取最后一个（通常是年份）

    # 策略 2：PDF 元数据
    try:
        doc = fitz.open(str(pdf_path))
        meta = doc.metadata
        creation_date = meta.get("creationDate", "") or meta.get("modDate", "")
        if creation_date:
            meta_year = re.findall(r"\b(19\d{2}|20\d{2})\b", creation_date)
            if meta_year:
                doc.close()
                return meta_year[0]
        doc.close()
    except Exception:
        pass

    # 策略 3：正文前 3 页寻找常见年份模式
    try:
        doc = fitz.open(str(pdf_path))
        head_text = ""
        for i in range(min(3, len(doc))):
            head_text += doc[i].get_text("text") + "\n"
        doc.close()

        # © 2024 / (c) 2024 / IEEE 2024 / 2024 IEEE 等模式
        patterns = [
            r"[©(c)C]\s*(19\d{2}|20\d{2})",
            r"(?:IEEE|ACM|Springer|Elsevier|Nature|Science|APS)\s+(19\d{2}|20\d{2})",
            r"(?:Received|Accepted|Published)\s*[:：]?\s*(?:\w+\s+)?(19\d{2}|20\d{2})",
        ]
        for p in patterns:
            matches = re.findall(p, head_text, re.IGNORECASE)
            if matches:
                return matches[0]
    except Exception:
        pass

    return "unknown"


def extract_text_from_pdf(pdf_path: Path) -> str:
    doc = fitz.open(str(pdf_path))
    pages = []
    for page in doc:
        pages.append(page.get_text("text"))
    doc.close()
    return "\n".join(pages)


def split_into_sections(full_text: str) -> dict:
    lines = full_text.split("\n")
    sections = {}
    current_section = "preamble"
    buffer = []

    for line in lines:
        stripped = line.strip()
        if SECTION_RE.match(stripped) and len(stripped) < 80:
            if buffer:
                sections[current_section] = "\n".join(buffer).strip()
            current_section = stripped[:60].lower().replace(" ", "_")
            buffer = []
        else:
            buffer.append(line)

    if buffer:
        sections[current_section] = "\n".join(buffer).strip()
    return sections


def tokenize(text: str) -> list:
    return re.findall(r"[a-zA-Z]+(?:[-'][a-zA-Z]+)*", text.lower())


def analyze_style_metrics(full_text: str, sections: dict) -> dict:
    """提取基础 + 分章节风格指标"""
    sentences = re.split(r"(?<=[.!?])\s+", full_text)
    sentences = [s.strip() for s in sentences if len(s.strip()) > 10]
    word_counts = [len(s.split()) for s in sentences]
    avg_words = sum(word_counts) / len(word_counts) if word_counts else 0
    long_ratio = sum(1 for w in word_counts if w > 30) / len(word_counts) if word_counts else 0
    short_ratio = sum(1 for w in word_counts if w < 10) / len(word_counts) if word_counts else 0

    # 被动语态
    passive_re = re.compile(
        r"\b(is|are|was|were|be|been|being)\s+\w+ed\b", re.IGNORECASE
    )
    passive_count = len(passive_re.findall(full_text))
    passive_ratio = passive_count / len(sentences) if sentences else 0

    # Hedging & Assertive 分项统计
    hedge_detail = {}
    for category, words in HEDGE_WORDS.items():
        for w in words:
            count = len(re.findall(r"\b" + re.escape(w) + r"\b", full_text, re.IGNORECASE))
            if count > 0:
                hedge_detail[w] = count

    assert_detail = {}
    for category, words in ASSERTIVE_WORDS.items():
        for w in words:
            count = len(re.findall(r"\b" + re.escape(w) + r"\b", full_text, re.IGNORECASE))
            if count > 0:
                assert_detail[w] = count

    total_hedge = sum(hedge_detail.values())
    total_assert = sum(assert_detail.values())

    # 分章节指标
    section_metrics = {}
    for sec_name, sec_text in sections.items():
        if len(sec_text) < 50:
            continue
        sec_sents = re.split(r"(?<=[.!?])\s+", sec_text)
        sec_sents = [s.strip() for s in sec_sents if len(s.strip()) > 10]
        if not sec_sents:
            continue
        sec_wc = [len(s.split()) for s in sec_sents]
        sec_passive = len(passive_re.findall(sec_text))
        sec_hedge = sum(
            len(re.findall(r"\b" + re.escape(w) + r"\b", sec_text, re.IGNORECASE))
            for words in HEDGE_WORDS.values() for w in words
        )
        sec_assert = sum(
            len(re.findall(r"\b" + re.escape(w) + r"\b", sec_text, re.IGNORECASE))
            for words in ASSERTIVE_WORDS.values() for w in words
        )
        section_metrics[sec_name] = {
            "sentence_count": len(sec_sents),
            "avg_words": round(sum(sec_wc) / len(sec_wc), 1) if sec_wc else 0,
            "passive_ratio": round(sec_passive / len(sec_sents), 3) if sec_sents else 0,
            "hedge_count": sec_hedge,
            "assert_count": sec_assert,
        }

    return {
        "total_sentences": len(sentences),
        "avg_words_per_sentence": round(avg_words, 1),
        "long_sentence_ratio": round(long_ratio, 3),
        "short_sentence_ratio": round(short_ratio, 3),
        "passive_voice_ratio": round(passive_ratio, 3),
        "hedging": {"total": total_hedge, "detail": hedge_detail},
        "assertive": {"total": total_assert, "detail": assert_detail},
        "hedge_assert_ratio": round(total_hedge / total_assert, 2) if total_assert > 0 else float("inf"),
        "section_metrics": section_metrics,
    }


def extract_frequent_words(full_text: str, top_n: int = 50) -> list:
    tokens = tokenize(full_text)
    filtered = [t for t in tokens if t not in STOP_WORDS and len(t) > 2]
    counter = Counter(filtered)
    return [{"word": w, "count": c} for w, c in counter.most_common(top_n)]


def analyze_connectors(full_text: str) -> dict:
    lower_text = full_text.lower()
    result = {}
    for category, words in CONNECTORS.items():
        category_stats = {}
        for w in words:
            count = len(re.findall(r"\b" + re.escape(w) + r"\b", lower_text))
            if count > 0:
                category_stats[w] = count
        if category_stats:
            result[category] = category_stats
    return result


def process_paper(pdf_path: Path, output_dir: Path) -> dict:
    print(f"  处理: {pdf_path.name}")
    year = extract_year_from_pdf(pdf_path)
    full_text = extract_text_from_pdf(pdf_path)
    sections = split_into_sections(full_text)
    metrics = analyze_style_metrics(full_text, sections)

    result = {
        "source": pdf_path.name,
        "year": year,
        "metrics": metrics,
        "sections": list(sections.keys()),
    }

    # JSON 输出
    out_file = output_dir / (pdf_path.stem + "_parsed.json")
    with open(out_file, "w", encoding="utf-8") as f:
        json.dump(result, f, ensure_ascii=False, indent=2)

    # 纯文本输出
    txt_file = output_dir / (pdf_path.stem + "_text.txt")
    with open(txt_file, "w", encoding="utf-8") as f:
        f.write(f"=== {pdf_path.name} ===\n\n")
        f.write(f"[METRICS]\n{json.dumps(metrics, indent=2)}\n\n")
        for sec_name, sec_text in sections.items():
            f.write(f"\n{'='*60}\n[SECTION: {sec_name}]\n{'='*60}\n")
            f.write(sec_text[:5000])
            if len(sec_text) > 5000:
                f.write("\n... [truncated] ...")
            f.write("\n")

    return result


def main():
    parser = argparse.ArgumentParser(description="批量解析导师 PDF 论文")
    parser.add_argument("input", help="PDF 文件或包含 PDF 的目录")
    parser.add_argument(
        "--output", default="./parsed_papers", help="输出目录（默认 ./parsed_papers）"
    )
    args = parser.parse_args()

    input_path = Path(args.input)
    output_dir = Path(args.output)
    output_dir.mkdir(parents=True, exist_ok=True)

    if input_path.is_file() and input_path.suffix.lower() == ".pdf":
        pdf_files = [input_path]
    elif input_path.is_dir():
        pdf_files = sorted(input_path.glob("**/*.pdf"))
    else:
        print(f"错误: {input_path} 不是有效的 PDF 文件或目录")
        sys.exit(1)

    if not pdf_files:
        print("未找到任何 PDF 文件")
        sys.exit(1)

    print(f"\n找到 {len(pdf_files)} 篇论文，开始解析...\n")

    all_metrics = []
    all_text = ""
    for pdf in pdf_files:
        try:
            m = process_paper(pdf, output_dir)
            m["paper"] = pdf.name
            # 防御性检查：确保 metrics 结构完整
            if "metrics" not in m or not isinstance(m["metrics"], dict):
                print(f"  警告: {pdf.name} 的 metrics 结构异常，已跳过")
                continue
            all_metrics.append(m)
            # 收集全文用于高频词和连接词分析
            doc = fitz.open(str(pdf))
            for page in doc:
                all_text += page.get_text("text") + "\n"
            doc.close()
        except Exception as e:
            print(f"  跳过 {pdf.name}: {e}")

    # 高频词分析
    freq_words = extract_frequent_words(all_text, top_n=50)
    freq_file = output_dir / "_frequent_words.json"
    with open(freq_file, "w", encoding="utf-8") as f:
        json.dump(freq_words, f, ensure_ascii=False, indent=2)

    # 连接词分析
    connectors = analyze_connectors(all_text)
    conn_file = output_dir / "_connector_words.json"
    with open(conn_file, "w", encoding="utf-8") as f:
        json.dump(connectors, f, ensure_ascii=False, indent=2)

    # 汇总统计
    if all_metrics:
        n = len(all_metrics)
        avg_sent_len = sum(m["metrics"]["avg_words_per_sentence"] for m in all_metrics) / n
        avg_passive = sum(m["metrics"]["passive_voice_ratio"] for m in all_metrics) / n
        total_hedge = sum(m["metrics"]["hedging"]["total"] for m in all_metrics)
        total_assert = sum(m["metrics"]["assertive"]["total"] for m in all_metrics)

        # 按年份分组统计
        year_groups = {}
        for m in all_metrics:
            y = m.get("year", "unknown")
            if y not in year_groups:
                year_groups[y] = []
            year_groups[y].append(m)

        year_summary = {}
        for y in sorted(year_groups.keys()):
            group = year_groups[y]
            gn = len(group)
            year_summary[y] = {
                "paper_count": gn,
                "avg_sentence_length": round(
                    sum(g["metrics"]["avg_words_per_sentence"] for g in group) / gn, 1
                ),
                "avg_passive_ratio": round(
                    sum(g["metrics"]["passive_voice_ratio"] for g in group) / gn, 3
                ),
                "total_hedge": sum(g["metrics"]["hedging"]["total"] for g in group),
                "total_assert": sum(g["metrics"]["assertive"]["total"] for g in group),
            }

        # 分章节指标汇总
        section_keys = set()
        for m in all_metrics:
            section_keys.update(m["metrics"]["section_metrics"].keys())

        section_summary = {}
        for sk in section_keys:
            vals = [m["metrics"]["section_metrics"].get(sk) for m in all_metrics
                    if sk in m["metrics"]["section_metrics"]]
            if vals:
                section_summary[sk] = {
                    "paper_count": len(vals),
                    "avg_words": round(sum(v["avg_words"] for v in vals) / len(vals), 1),
                    "avg_passive_ratio": round(
                        sum(v["passive_ratio"] for v in vals) / len(vals), 3
                    ),
                    "avg_hedge": round(sum(v["hedge_count"] for v in vals) / len(vals), 1),
                    "avg_assert": round(sum(v["assert_count"] for v in vals) / len(vals), 1),
                }

        # 连接词 Top 5（标注首选）
        top_connectors = {}
        for cat, words in connectors.items():
            sorted_words = sorted(words.items(), key=lambda x: x[1], reverse=True)[:3]
            top_connectors[cat] = sorted_words

        summary = {
            "papers_analyzed": n,
            "year_range": (
                f"{min(year_groups.keys())}-{max(year_groups.keys())}"
                if all(y != "unknown" for y in year_groups) else "unknown"
            ),
            "year_summary": year_summary,
            "avg_sentence_length_words": round(avg_sent_len, 1),
            "avg_passive_voice_ratio": round(avg_passive, 3),
            "total_hedging_words": total_hedge,
            "total_assertive_words": total_assert,
            "hedge_assert_ratio": round(
                total_hedge / total_assert, 2
            ) if total_assert > 0 else "inf",
            "style_tendency": (
                "偏保守/谨慎" if total_hedge > total_assert * 1.5 else
                "中性平衡" if total_hedge > total_assert * 0.7 else
                "偏自信/直接"
            ),
            "section_summary": section_summary,
            "top_connectors": top_connectors,
        }

        summary_file = output_dir / "_summary.json"
        with open(summary_file, "w", encoding="utf-8") as f:
            json.dump(summary, f, ensure_ascii=False, indent=2)

        print(f"\n解析完成，结果保存至: {output_dir}")
        print(f"\n汇总统计:")
        print(f"  分析论文数: {summary['papers_analyzed']}")
        print(f"  年份范围: {summary['year_range']}")
        if year_summary:
            print(f"  按年份分布:")
            for y in sorted(year_summary.keys()):
                ys = year_summary[y]
                print(f"    {y}: {ys['paper_count']} 篇 | 平均句长 {ys['avg_sentence_length']} 词 | 被动语态 {ys['avg_passive_ratio']:.1%} | hedge/assert {ys['total_hedge']}/{ys['total_assert']}")
        print(f"  平均句长: {summary['avg_sentence_length_words']} 词")
        print(f"  被动语态比例: {summary['avg_passive_voice_ratio']:.1%}")
        print(f"  Hedging/Assertive 比值: {summary['hedge_assert_ratio']}")
        print(f"  写作倾向: {summary['style_tendency']}")
        print(f"  高频词 Top 10: {', '.join(w['word']+'('+str(w['count'])+')' for w in freq_words[:10])}")
        print(f"\n输出文件:")
        print(f"  汇总: {summary_file}")
        print(f"  高频词: {freq_file}")
        print(f"  连接词: {conn_file}")


if __name__ == "__main__":
    main()
