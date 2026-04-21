# 导师写作风格卡片

> 导师：Guo Chuan Fei (郭传飞) | 学科：柔性电子 / 离子电子学 (Flexible Electronics / Iontronics) | 分析论文数：22 篇 | 年份范围：2020-2025 | 分析日期：2026-04-21
> 数据来源：22 篇 PDF 论文（Nature Communications、Science Advances、Advanced Materials、Advanced Functional Materials、NPG Asia Materials 等）
> 风格基准期：2022-2025（共 16 篇，占总数 73%）

---

## 一、核心风格画像（通过三重验证）

以下每个模式都通过了 ≥2 重验证（跨篇复现 + 生成力 + 排他性）。

### 1.1 宏观结构

- **Introduction**：4-6 段，CARS Move 顺序为 背景(1-2段) → 现有方法不足(1-2段) → Gap 指出 → 本文贡献(末段)
- **Introduction 篇幅**：极紧凑，占全文 **3-8%**（多数 100-150 词），信息密度极高
- **Contribution 格式**：**100% 叙事句**（22/22），绝不使用 bullet list。在 Introduction 末段用 "In this work, ..." / "Herein, we demonstrate ..." 引出，2-3 个贡献点连贯呈现
- **Related Work**：**22/22 无独立章节**，相关工作融入 Introduction，通过引用密集段落展示文献掌握
- **Results & Discussion**：部分合并为 "Results and Discussion"，部分分开。数据呈现先图后文
- **Conclusion**：1 段（100-150 词），不重述 contribution 逐条，概括核心发现 + 应用前景收尾
- **Future Work**：无独立小节，通过 "expected to" / "This work opens" 嵌入末句
- **小节命名风格**：数字编号 + 简短描述性短语（"Sensing mechanism and finite element analysis"、"Fabrication of high-porosity dielectric layer"）

### 1.2 句式指纹

| 指标 | 数值 |
|------|------|
| 平均句长 | 18.1 词（学术写作偏短，信息密度高） |
| 长句（>30词）比例 | 13.1% |
| 短句（<10词）比例 | 33.4% |
| 被动语态比例（全局） | 20.8%（偏低，强调主动贡献） |

**分章节语态差异**（四部分句长递减规律）：
- Introduction/Preamble：句长 29-37 词，被动 17-24%（主动为主）
- Methods：句长 16-22 词，被动 **54-84%**（全篇最高，被动为主）
- Results：句长 14-22 词，被动 12-27%（混合）
- Discussion：句长 20-27 词，被动 31-62%（偏被动）

**句首 Subject 偏好**：
| 类型 | 比例 | 示例 |
|------|------|------|
| "The + 名词" | ~35% | "The sensor shows..." |
| "We + 动词" | ~25% | "We demonstrate..." |
| "This + 名词" | ~15% | "This approach..." |
| "In this + 名词" | ~10% | "In this work..." |
| 被动开头 | ~10% | "A film was..." |

**时态规律**：
| 章节 | 时态 | 功能 |
|------|------|------|
| Introduction | 现在时 | 描述背景和现状 |
| Methods | 过去时 | 描述实验过程 |
| Results | 现在时 | 陈述发现 |
| Conclusion | 现在时 | 表达意义 |

### 1.3 Hedging & 断言

- **Hedging 总频**：274 次 | **Assertive 总频**：335 次
- **比值**：0.82 → 风格倾向：**中性平衡，略偏断言**（处于健康区间 0.7-1.2）

**三层 hedging 策略**（贯穿全部 22 篇）：
- **材料/方法描述** → 强 claim（we propose/present，无 hedging）
- **性能声明** → 中等-强 claim（数据支撑的 demonstrate/show/exhibit）
- **影响/前景声明** → 弱 claim（may/could/expected to/potentially）

**最常用 hedging 词汇**：may, can, could, indicate, potentially, suggest, approximately, relatively, might, likely

**最常用 assertive 词汇**：show(最高频), exhibit, demonstrate, significantly, reveal, confirm, present, notably, remarkably, substantially, achieve, enable

**分章节 hedging 分布**：
- Introduction：中等（每篇 4-8 个），策略性组合"自信提出 + 谨慎限定"
- Results：极少 hedging，以 exhibit/show/reveal 为主
- **Discussion：hedging 最密集**，大量 suggest/indicate/could be attributed to
- Conclusion：显著降低 hedging，以 demonstrate/show/prove/enable 为主

**数值表述**：
- 实验数据 → 精确到小数点（如 "23.6 kPa", "0.027 N·m"）
- 性能对比 → 近似+比较级（"approximately 3-fold higher than"）
- 检测限/范围 → "up to / as low as" + 精确数值
- 近似词用 "approximately" 而非 "about/around"

### 1.4 论证逻辑

- **问题引入方式**：**应用驱动 + 仿生类比**。从实际应用场景（电子皮肤、正畸力监测、眼压监测）或自然界现象（"human skin"、"skin-like"）切入
- **四段式论证链**：现象观察 → 机制假设 → 实验验证 → 性能/应用展示
- **Gap 识别策略**："However/Despite/Although" 转折，指出现有方法在灵敏度、线性度、范围、稳定性等指标不足
- **Contribution 声明格式**（高度模式化）：
  - "In this work, we propose/present/develop [方法] for [应用]"
  - "Herein, we demonstrate/report [方法] that achieves [指标]"
  - "This work provides/fabricates/explores [方法]"
- **Contribution 三层结构**：①核心贡献（新方法/材料/机制）→ ②性能贡献（达到优异指标）→ ③应用贡献（展示实际场景）
- **对比批评语气**：**温和但有据**。不直接否定前人工作，通过性能指标差异体现优势
- **因果表述**：正向 "Due to the...structure, the sensor exhibits..."；反向 "The behavior can be attributed to..."
- **逻辑链完整性**：22/22 具有完整的 "应用场景 → 技术需求 → 现有方法不足 → 本文方案 → 贡献" 链条

### 1.5 图表叙事

- **叙事链**：Figure 1(表征) → Figure 2(机理) → Figure 3(性能) → Figure 4(应用)
- **Caption 风格**：**详细描述型**，2-4 句，包含内容说明 + 关键发现概括
- **Caption 命名模式**："Figure X. [核心发现动词] + [研究对象]"（如 "Fabrication and characterization of the iontronic sensor"）
- **首选图表引用句式**：
  - "As shown in Fig. X, ..."（**最常用**）
  - "Figure X shows that ..."
  - "The results in Fig. X demonstrate/indicate ..."
- **引用偏好**：**后置引用**（先描述数据结果，再指向图表），如 "The sensitivity reaches 5.8 kPa⁻¹, as shown in Fig. 3a"
- **多图联动**：常使用 "Fig. 1a-d" 多子图协同叙事
- **数据描述模板**：
  - "The sensor exhibits a sensitivity of X kPa⁻¹ within the range of Y–Z kPa"
  - "The sensitivity reaches X kPa⁻¹ at Y kPa, which is [N] times higher than that of [对比对象]"
  - "The device shows a linear response (R² = X) over a broad pressure range of Y–Z kPa"
- **对比表述**："compared with/compared to"（最常用）| "exhibits higher/lower ... than"（常用）| "outperforms"（偶用）
- **补充材料引用**："Additional results are shown in Supplementary Fig. X"

### 1.6 表达 DNA

- **风格标签**：正式=高 | 具体>抽象 | 断言=中性偏强 | 句长=中等偏短 | 铺垫型 | 数据驱动
- **首选连接词**：
  - 递进：**also**(251, 远超其他) | in addition(83) | furthermore(52)
  - 转折：**while**(140) | however(93) | but(92) | although(46)
  - 因果：**thus**(86) | therefore(62) | as a result(34)
  - 总结：**overall**(29) | finally(26) | **"in conclusion" 几乎不用**
  - 举例：**such as**(105) | for example(38)
- **引用嵌入方式**：
  - "[数字]" 上标格式（Nature/Science 系列风格）
  - "Previous studies have demonstrated [内容] [1-5]"
  - 偶用作者名引用："as reported by Smith et al."
- **口癖（标志性表达）**：
  - "In this work, we ..." / "Herein, we demonstrate ..."（22/22，Introduction 末段）
  - "As shown in Fig. X, ..."（每篇 10+ 次，极高频率）
  - "The sensor exhibits ..."（性能描述标准句式）
  - "enables ... applications"（应用展望惯用搭配）
  - "is crucial/essential for ..."（强调重要性）
  - "high sensitivity and high linearity"（高频性能组合）
  - "becomes imperative"（表达必要性）
  - "burgeoning"（形容新兴技术）
- **个人风格标记词**（vs 领域通用）：
  - **ionic/iontronic**（所有论文稳定出现，个人学术标签）
  - exhibit（描述性能首选动词）
- **禁忌/回避表达**：
  - "very"（用 highly/significantly 替代）
  - "in conclusion" / "to sum up"（偏好自然收束或 "In summary"）
  - 口语化连接词（plus, anyway）
  - 过于绝对否定（cannot, never → 用 "fails to" / "is limited by"）
  - 极端肯定词（definitely, prove 罕见，多用 demonstrate）
  - 情感词（exciting, amazing → 保持客观）

---

## 二、分章节写作指南

### 2.1 Introduction

**典型结构**（4-6 段，100-150 词）：
1. 段1：应用场景切入（电子皮肤、可穿戴设备等）或仿生类比（"Human skin can perceive..."）
2. 段2-3：现有方法综述 + "However/Despite" 指出不足（灵敏度、线性度、范围、稳定性）
3. 段4-5：提出本文方案，核心设计思路，"Herein, we demonstrate ..."
4. 段6（可选）：论文结构概览

**本节特殊偏好**：
- 句长：平均 29-37 词（全篇最长，信息密度最高）
- 语态：主动为主（被动 17-24%）
- Hedging：contribution 声明不用 hedging（直接断言）
- **绝不使用 bullet list** 列 contribution
- 段首常用："Flexible pressure sensors have attracted ..." / "The measurement of X is crucial for ..." / "In recent years, ..."

**可复用句式**：
```
"[应用场景] has attracted considerable attention due to its potential applications in ..."
"However, existing sensors still suffer from [问题1] and [问题2], limiting their practical applications."
"In this work, we propose/present/develop [方法] for [应用], which achieves [关键指标]."
"Herein, we demonstrate that [策略] achieves [性能], enabling [应用方向]."
"The design of [方法] enables [优势1], [优势2], and [优势3]."
```

### 2.2 Methods

**典型结构**：按实验流程分小节（材料制备 → 器件组装 → 表征方法），数字编号

**本节特殊偏好**：
- 小节命名：动词性/描述性短语（"Fabrication of ...", "Characterization and measurements"）
- 公式/伪代码密度：低（以文字描述为主）
- 句长：平均 16-22 词
- 语态：**被动语态 54-84%**（全篇最高）
- 补充材料："Details are provided in Supplementary Information / Supplementary Fig. X"

**可复用句式**：
```
"The [材料] was prepared by mixing [成分] at a ratio of [比例]."
"The fabrication process is illustrated in Fig. X."
"Characterization was performed using [仪器/方法]."
```

### 2.3 Results

**典型结构**：按性能维度分小节（灵敏度 → 线性度 → 响应时间 → 稳定性 → 应用展示），每节一个主题

**图表叙事链**：Figure 1(表征) → Figure 2(机理) → Figure 3(性能) → Figure 4(应用)

**本节特殊偏好**：
- 数据呈现：**后置引用**（先描述数据，再引用图表）
- 图表引用密度极高（每 2-3 句一次引用）
- 多图联动："Fig. 1a-d" 子图协同
- 数值精度：保留 2-3 位有效数字，大数用科学计数法

**可复用句式**：
```
"As shown in Fig. X, the sensor exhibits a sensitivity of X kPa⁻¹ within Y–Z kPa."
"The sensitivity reaches X kPa⁻¹ at Y kPa, which is [N] times higher than that of [对比对象]."
"The device shows a linear response (R² = X) over a broad pressure range of Y–Z kPa."
"Compared with [方法], our sensor demonstrates superior [性能] performance."
```

### 2.4 Discussion

**典型结构**：较短（1-2 段），合并或独立，讨论传感机制和物理原理

**本节特殊偏好**：
- 句长：平均 20-27 词（全篇较长）
- 被动语态偏高（31-62%）
- **Hedging 最密集的章节**，大量 suggest/indicate/could be attributed to
- 常用机制解释句式

**可复用句式**：
```
"The enhanced performance can be attributed to [机制]."
"This [现象] is consistent with [理论/前人结果]."
"The behavior can be attributed to [原因], resulting in [结果]."
"The results indicate that [方法] holds promise for [应用方向]."
```

### 2.5 Conclusion

**典型结构**：1 段（100-150 词），不分点。概括核心发现 + 应用前景

**本节特殊偏好**：
- 不逐条重述 contribution
- **Hedging 显著降低**，以 demonstrate/show/prove/enable 为主
- 末句以应用前景收尾（"enables ... applications"）
- 被动语态偏高（28-60%）
- 无独立 Future Work，前瞻性表述嵌入末句
- **不用 "In conclusion" 开头**，偏好 "In summary" 或直接陈述

**可复用句式**：
```
"In summary, we have demonstrated [方法] for [应用]."
"The [方法] achieves [关键指标], enabling [应用前景]."
"This work provides a promising approach for [方向]."
"The proposed method is expected to be applied in [应用场景]."
```

---

## 三、偶发特征附录

以下特征未通过三重验证（仅 1 重验证），不作为核心风格，但值得了解：
- **"Here, we report" 开头**：仅出现在 Science Advances 论文中（3/22），其他期刊偏好 "In this work, we"
- **"In this article, we have summarized" 开头**：仅出现在综述论文中（1/22）
- **独立 Discussion 章节**：取决于期刊格式（Nature 系列有，Adv. Mater 系列无），非导师主动选择
- **数值用分数表示**（如 "2/3 of"）：仅偶见
- **H/A 比值波动 >1.0**：2021 年（1.21）和 2023 年（1.50）对应进入新研究方向，属合理的学术行为

---

## 四、风格矛盾记录

| 类型 | 矛盾描述 | 处理 |
|------|---------|------|
| 时间演化 | 被动语态从 2022 年 26% 下降到 2024 年 17%；assertive 词从 2022 年大幅增长后保持 | 以 2022-2025 近期为主 |
| 论文类型 | Science Advances 偏简洁（句长 14.7），Nature Communications 偏正式（句长 18-20） | 期刊格式差异，以 Nat Commun/Adv Mater 风格为主 |
| 章节差异 | Methods 被动 54-84% vs Introduction 17-24% | 正常章节差异 |
| 研究阶段 | 进入新方向时 H/A 升高（2021、2023），方法成熟时 H/A 降低（2022、2024-25） | 合理的学术行为，非风格矛盾 |

### 年份演化轨迹

| 年份区间 | 论文数 | 平均句长 | 被动语态 | H/A 比值 | 显著变化 |
|---------|-------|---------|---------|---------|---------|
| 2020-2021 | 3 | 17.4 词 | 21.4% | 1.04 | 基准期，hedging 略多 |
| 2022 | 4 | 19.0 词 | 26.0% | 0.56 | 句长峰值，被动最高，assertive 增多 |
| 2023 | 3 | 17.1 词 | 21.2% | 1.50 | 进入新领域，hedging 回升 |
| 2024-2025 | 9 | 18.2 词 | 17.6% | 0.73 | 被动降低，风格稳定，更简洁直接 |

**趋势总结**：导师写作风格趋于**更简洁、更直接、更主动**。被动语态下降、assertive 词汇增多是明显趋势。2024-2025 H/A 稳定在 ~0.73，风格已成熟定型。

---

## 五、诚实边界

- 本卡片基于 22 篇论文分析，其中大部分为导师通讯作者论文
- **Conclusion 样本不足**：脚本仅识别到 2 篇的独立 Conclusion 章节，其余被合并或解析不完整，该维度置信度中等
- **"can" 未计入 hedging 统计**：脚本词表未包含 "can"，但 Agent3 分析发现 "can" 实际使用 ~65 次，是最频繁的 hedging/能力词。真实的 H/A 比值可能更低
- 合著论文可能混杂学生写作风格，特别是第一作者段落的表达可能不代表导师风格
- 论文分布在不同期刊，期刊格式要求可能导致部分结构特征是期刊约束而非个人偏好
- 建议每 6-12 个月更新一次，纳入新发表论文

---

## 六、快速参考卡片（用于写作时速查）

```
句长目标：        18 ± 3 词（Introduction 可放宽到 30-35 词）
被动语态：        全局 ~21%，Methods 节 54-84%，Introduction ~20%
Hedging 倾向：    中性（H/A ≈ 0.8）
                  Introduction: 贡献声明不用 hedging
                  Discussion: hedging 最密集
                  Conclusion: hedging 显著降低
首选连接词：      递进=also/in addition | 转折=while/however
                  因果=thus/therefore | 举例=such as
                  总结=overall/finally（不用 "in conclusion"）
Contribution：    连续段落（绝不 bullet），"In this work, we ..."
数据描述：        "The sensor exhibits a sensitivity of X kPa⁻¹ within Y–Z kPa"
图表引用：        "As shown in Fig. X, ..."（后置引用）
                  多图联动 "Fig. 1a-d"
Caption 命名：    "Figure X. [动词] + [研究对象]"
因果表述：        "Due to ...structure, ..." / "can be attributed to ..."
绝不使用：        very（用 highly/significantly）
                  in conclusion（用 In summary）
                  口语化连接词（plus, anyway）
                  过于绝对否定（cannot, never → fails to / is limited by）
                  情感词（exciting, amazing）
引用格式：        "[数字]" 上标
补充材料：        "Supplementary Information / Supplementary Fig. X"
应用展望：        "enables ... applications" / "is expected to be applied in ..."
```

---

## 使用说明

- **写作辅助时**：AI 读取卡片中对应章节指南，作为写作约束
- **润色检查时**：逐条对照快速参考卡片的参数范围
- **更新时**：增量修改变化项，保留不变项，在卡片顶部更新日期和样本数
- 本卡片版本：v1.0 | 生成日期：2026-04-21
