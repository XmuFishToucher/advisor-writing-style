# 学术写作风格分析框架

从导师论文中提炼可运行的写作风格模型的核心方法论。

---

## 一、写作模式三重验证

一个写作特征要被认定为「核心风格」而非「偶发行为」，必须通过三重验证：

### 验证 1：跨篇复现
同一模式出现在 ≥50% 的已分析论文中。

例：如果导师在 8/10 篇论文的 Introduction 中都用「问题驱动」引入方式 → 跨篇复现 → 核心风格。
如果某种 hedging 词汇只在 2/10 篇中出现 → 未通过 → 降级为偶发特征。

### 验证 2：有生成力
用这个模式能推断导师对新内容的写法。

例：如果导师惯用「先图后文」呈现数据 → 面对新实验结果时也能推断他会先放图 → 有生成力 → 核心风格。

### 验证 3：有排他性
不是该领域所有论文都这样写，体现导师个人偏好。

例：「主动语态声明 Contribution」在很多顶会论文中常见 → 无排他性 → 标注为「领域通用」。
但导师特有的「用反问句过渡到 Related Work」→ 有排他性 → 标注为「导师独特」。

**通过 0 验证** → 丢弃
**通过 1 验证** → 降级为「偶发特征」，放入附录
**通过 2-3 验证** → 纳入核心风格卡片，标注验证结果

---

## 二、六大采集维度

### 维度 1：宏观结构

#### 1.1 Introduction 结构（CARS 模型 + 变体）
- **Move 1 — 建立研究领域**：背景铺陈占几段？宏观切入 vs 直接进入问题？
- **Move 2 — 建立研究空间**：如何指出现有方法不足？"However" 硬转 vs 层层递进？
- **Move 3 — 占据研究空间**：Contribution 呈现方式？bullet list / 连续句 / 混合？
- 典型段落数：___ | 典型字数占全文比例：___

#### 1.2 Methods 结构
- 是否有独立 Related Work 节？
- 小节命名风格（描述性 `3.1 Feature Extraction` vs 动词性 `3.1 Extracting Features`）
- 公式/伪代码/流程图使用频率

#### 1.3 Results & Discussion
- Results 和 Discussion 合并还是分开？
- 数据呈现顺序：先图后文 vs 先文后图？
- 实验对比组织方式：按数据集 / 按 baseline / 按 ablation

#### 1.4 Conclusion
- 是否重述 contribution？
- Limitation 位置（Conclusion 内 vs 独立小节）
- Future Work 表述（具体 vs 泛化）

---

### 维度 2：句式指纹

从每篇论文中随机抽取 20 个段落，统计：

| 指标 | 测量方式 | 导师数据 |
|------|---------|---------|
| 平均句长（词数） | 总词数 / 总句数 | ___ |
| 长句（>30词）比例 | 长句数 / 总句数 | ___ |
| 短句（<10词）比例 | 短句数 / 总句数 | ___ |
| 复合句偏好 | 并列 / 从属 / 混合 | ___ |

**分章节统计**（关键差异通常在这里）：

| 章节 | 平均句长 | 被动语态比例 | 主动语态比例 |
|------|---------|-------------|-------------|
| Introduction | ___ | ___% | ___% |
| Methods | ___ | ___% | ___% |
| Results | ___ | ___% | ___% |
| Discussion | ___ | ___% | ___% |
| Conclusion | ___ | ___% | ___% |

#### 风格标签定位

从以下 7 个维度打标：

```
正式 ←→ 口语
抽象 ←→ 具体
谨慎 ←→ 断言
学术 ←→ 通俗
长句 ←→ 短句
铺垫型 ←→ 结论先行
数据驱动 ←→ 叙事驱动
```

每个维度标记导师的位置（不是极端，标注偏向和程度）。

---

### 维度 3：Hedging & 断言策略

#### Hedging 词汇统计
- **情态动词**：may / might / could / should — 各出现 ___ 次
- **认知动词**：suggest / indicate / appear / seem / tend to — 各出现 ___ 次
- **程度副词**：approximately / generally / typically / relatively / potentially — 各出现 ___ 次

#### Assertive 词汇统计
- **证明类**：demonstrate / prove / confirm / establish — 各出现 ___ 次
- **展示类**：show / reveal / illustrate / exhibit — 各出现 ___ 次
- **强调副词**：significantly / notably / remarkably / clearly / obviously — 各出现 ___ 次

#### Hedging 强度判断
- Hedging 总频 / Assertive 总频 比值：___
- □ 强保守（比值 > 1.5）
- □ 中性平衡（比值 0.7-1.5）
- □ 偏自信（比值 < 0.7）

#### 分章节差异
Introduction 和 Conclusion 的 hedging 策略是否与 Methods/Results 不同？（通常是的，需要记录）

---

### 维度 4：论证逻辑

#### 4.1 问题引入方式
- **问题驱动**：先描述应用场景痛点 → 引出技术挑战
- **方法驱动**：先回顾现有技术树 → 指出空白
- **数据驱动**：先展示规律/现象 → 提出解释需求
- **混合型**：以上两种以上组合使用

#### 4.2 Contribution 呈现
提取具体原文：
```
"The main contributions of this paper are as follows:"
"In summary, this paper makes the following contributions:"
"Our key contributions include:"
```
- Contribution 条目数：通常 ___ 条
- 每条字数：___ 词
- 是否有层级（主贡献 + 子贡献）

#### 4.3 Related Work 处理
- 独立节 vs 融入 Introduction？
- 组织维度：按方法类型 / 按时间线 / 按问题类型
- 对比语气：直接指出缺陷 vs 委婉表达局限
- 是否在 Introduction 就开始与相关工作对比？

---

### 维度 5：图表叙事

#### 5.1 Caption 风格
- □ 简短描述型：`Figure 1: Overview of our proposed method.`
- □ 详细说明型：`Figure 1: Overview of the proposed framework. (a) shows... (b) illustrates...`

#### 5.2 图表引用句式
统计各句式出现频次：
- `As illustrated in Figure X, ...` — ___ 次
- `Figure X shows that ...` — ___ 次
- `The results in Table X demonstrate ...` — ___ 次
- `We can observe from Figure X that ...` — ___ 次

#### 5.3 实验数据描述模板
提取导师常用的数值表述：
```
"Our method achieves [X]% [metric] on [dataset], outperforming [baseline] by [delta]."
"As shown in Table X, [method] consistently outperforms all baselines across [conditions]."
"The proposed approach reduces [metric] by [X]% compared to [baseline]."
```

---

### 维度 6：表达 DNA

#### 6.1 高频词汇 Top 20
从全部论文中提取去除停用词后的 Top 20 高频词汇（排除领域通用术语）。

#### 6.2 连接词偏好
统计各连接词使用频次：
- 递进：Furthermore / Moreover / In addition / Additionally
- 转折：However / Nevertheless / Nonetheless / In contrast
- 因果：Therefore / Consequently / As a result / Thus
- 总结：In summary / To summarize / Overall / In conclusion
- 举例：For example / For instance / Specifically / In particular

标注导师的「首选连接词」（某类别中频率显著高于其他的）。

#### 6.3 引用嵌入方式
- `[X] proposed` — ___ 次
- `X et al. showed` — ___ 次
- `As reported by X` — ___ 次
- `Following the approach in [X]` — ___ 次
- 簇引用 vs 散引用偏好

#### 6.4 禁忌词 & 口癖
- **导师从不用的表达**：从全部论文中未出现但同类论文中常见的表达
- **导师口癖**：出现频率异常高的特定短语/句式（标注为口癖但提醒使用频率上限）

---

## 三、年份演化分析

论文按发表年份分组，追踪风格随时间的演变轨迹。

### 分析方法

1. 将论文按年份分组（脚本自动输出 `_summary.json` 中的 `year_summary`）
2. 对比以下指标在不同年份组间的变化：
   - 平均句长（变长 → 更复杂？变短 → 更简洁？）
   - 被动语态比例（升高 → 更正式？降低 → 更主动？）
   - Hedging/Assertive 比值（变化 → 更自信/更谨慎？）
   - Contribution 条目数（变化 → 更聚焦/更全面？）

### 演化轨迹记录格式

| 年份区间 | 论文数 | 平均句长 | 被动语态 | H/A 比值 | 显著变化 |
|---------|-------|---------|---------|---------|---------|
| 2018-2020 | N 篇 | ___ | ___% | ___ | [描述] |
| 2021-2023 | N 篇 | ___ | ___% | ___ | [描述] |
| 2024-2026 | N 篇 | ___ | ___% | ___ | [描述] |

### 判断规则
- 变化 < 10% → 标注为「稳定」，不纳入矛盾
- 变化 10-30% → 标注为「渐进演化」，在风格卡片中注明
- 变化 > 30% → 标注为「显著变化」，需要判断以哪个时期为主

---

## 四、矛盾处理原则

矛盾是真实风格的体现，不是 Bug。

| 矛盾类型 | 示例 | 处理 |
|---------|------|------|
| **时间演化** | 早期 hedging 多，近期更自信 | 参照第三节年份演化分析，以近期为主，标注「早期特征」 |
| **论文类型** | 期刊更正式，会议偏口语 | 分类型记录，不强行统一 |
| **章节差异** | Intro 主动多，Methods 被动多 | 分章节记录，标注为「正常章节差异」 |

**错误处理**：选一边忽略另一边 / 编调和解释 / 假装矛盾不存在

---

## 五、信息不足处理

| 情况 | 处理 |
|------|------|
| 论文 < 5 篇 | 全局标注「低置信度」，每个模式标注样本数 |
| 某章节样本少 | 该维度降级，不纳入核心卡片 |
| 扫描版 PDF 提取失败 | 提示 OCR，标注「此篇未纳入」 |
| 合著论文风格混杂 | 优先选导师唯一通讯作者的论文，标注「合著置信度低」 |

---

## 六、质量自检清单

风格卡片生成后，逐条检查：

### 核心风格
- [ ] 每个核心模式都通过了 ≥2 重验证？
- [ ] 核心模式数量在 5-15 个之间？（太少=太浅，太多=没提炼）
- [ ] 每个模式都有来自论文的具体证据（原文引用）？

### 句式指纹
- [ ] 数据来自 ≥5 篇论文？
- [ ] 分章节统计完整（至少覆盖 Introduction + Methods + Results）？

### 表达 DNA
- [ ] 高频词汇排除了领域通用术语？
- [ ] 口癖标注了使用频率上限（避免模仿过头）？
- [ ] 禁忌词列表具体可操作（不是「避免口语化」这种模糊说法）？

### 写作模板
- [ ] 有至少 3 个可直接复用的模板（Contribution / 数据描述 / 图表引用）？
- [ ] 模板来自 ≥3 篇论文的共性提炼？

### 诚实边界
- [ ] 明确标注了哪些维度信息不足？
- [ ] 标注了论文样本数和学科领域？
- [ ] 承认了合著混杂等已知局限？

### 整体
- [ ] 删掉导师名字后，卡片仍能独立指导写作？
- [ ] 不是原始文本的拼凑，而是可运行的风格框架？
- [ ] 一个不了解导师的人用这个卡片写出来的论文，导师会认可风格？
- [ ] 年份演化是否已分析？是否存在 >30% 的显著变化？
- [ ] 风格卡片以哪个时期的风格为主？是否已标注？
