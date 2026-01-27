# AI-Financial-Insight

## What is AI-Financial-Insight?

- 一个从 0 到 1 的「财经情绪分析」全栈小项目。(练习学习向)

## goal

- 通过关键词分析情绪统计结果

## MVP(Phase 1)

### 1）backend(flask)

- 情绪分析接口（核心）

  接口内部做什么？

  1. 接受关键词
  2. 获取10条相关文本
  3. 对每条文本做情感分析
  4. s统计正负面数量
  5. 返回json

### 2）AI情感分析

1. 规则
2. TextBlob
3. HuggingFace sentiment pipeline

### 3）数据来源

当前版本使用简化数据源，重点验证系统流程，后续可扩展实时爬虫

###4）前端（vue)

