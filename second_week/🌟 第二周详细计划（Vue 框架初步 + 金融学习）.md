非常好 👍！第二周是整个“AI理财助手项目”的 **前端学习与雏形搭建阶段**，
 这一周的目标是：

> 掌握 Vue 基础语法 + Axios 调用 + 搭出一个能展示静态数据的首页雏形（为后端连接做准备）。

同时你希望**包含金融学习任务**，我已经帮你平衡安排好：每天约 4~5 小时技术学习 + 1~2 小时金融知识巩固。

------

# 🌟 第二周详细计划（Vue 框架初步 + 金融学习） #

📅 周期：**10.25 - 10.31**

------

## 🧱 本周目标 ##

| 模块 | 目标                                                    |
| ---- | ------------------------------------------------------- |
| 前端 | 熟悉 Vue 语法、组件系统、Axios 请求、ECharts 初步使用   |
| 工具 | 理解 npm、Vite、项目结构、组件运行原理                  |
| 金融 | 学习股票基础与行情数据结构（为数据展示打基础）          |
| 结果 | 能运行一个 Vue + ECharts 静态页面（显示虚拟股票行情图） |

------

## 📅 Day 1：Vue 项目运行与结构理解 ##

**目标：** 能运行一个 Vite + Vue 项目并理解各文件作用。

### 🧩 技术任务： ###

1. 打开你之前用 Node + Vite 创建的项目（`AI-Financial-Insight`）
    如果不确定，还可以重新初始化：

   ```bash
   npm create vite@latest
   ```

   然后选：

   ```
   Project name: AI-Financial-Insight
   Framework: Vue
   Variant: JavaScript
   ```

2. 安装依赖：

   ```bash
   npm install
   npm run dev
   ```

3. 理解项目结构：

   - `src/App.vue`：主界面
   - `src/components/`：放小组件
   - `main.js`：项目入口
   - `index.html`：网页模板

4. 修改首页文字：
    打开 `App.vue`，把 `<template>` 中的内容换成：

   ```vue
   <template>
     <h1>AI 理财助手主页</h1>
     <p>欢迎来到 AI Financial Insight</p>
   </template>
   ```

✅ **输出结果：** 浏览器成功显示新标题。

------

### 📚 金融学习： ###

- 阅读资料：《小白理财入门》第1章——股票与基金区别。
- 看视频（B站推荐关键词）：**“股票基础入门10分钟”**
- 任务：理解“股票代码”、“开盘价”、“收盘价”的含义。

------

## 📅 Day 2：Vue 基础语法 + 数据绑定 ##

**目标：** 掌握 Vue 模板语法与数据绑定。

### 🧩 技术任务： ###

1. 在 `App.vue` 中加入响应式数据：

   ```vue
   <script setup>
   import { ref } from 'vue'
   const stockName = ref('AAPL')
   const stockPrice = ref(185.12)
   </script>
   
   <template>
     <h2>{{ stockName }} 当前价格：{{ stockPrice }}</h2>
   </template>
   ```

2. 学习内容：

   - `ref()` 的用法
   - `v-if`, `v-for`, `v-bind`, `v-on` 基本语法
      （用官方教程或 Vue3 中文网：https://cn.vuejs.org/）

3. 练习小项目：

   - 制作一个可以点击按钮涨价/跌价的股票卡片。

✅ **输出结果：** 能点击按钮动态修改股票价格。

------

### 📚 金融学习： ###

- 学习内容：“K线图”基础知识（阴线阳线代表什么）
- 视频推荐：《K线图快速看懂股票涨跌（小白版）》
- 任务：自己画出一张简单的K线图示意。

------

## 📅 Day 3：组件化 + Props 传参 ##

**目标：** 学会拆分 Vue 组件。

### 🧩 技术任务： ###

1. 新建文件：`src/components/StockCard.vue`

   ```vue
   <script setup>
   defineProps(['name', 'price'])
   </script>
   
   <template>
     <div class="card">
       <h3>{{ name }}</h3>
       <p>当前价格：{{ price }}</p>
     </div>
   </template>
   
   <style scoped>
   .card { border: 1px solid #ccc; padding: 10px; border-radius: 10px; }
   </style>
   ```

2. 在 `App.vue` 中引用：

   ```vue
   <script setup>
   import StockCard from './components/StockCard.vue'
   </script>
   
   <template>
     <StockCard name="AAPL" price="185.12" />
     <StockCard name="TSLA" price="247.31" />
   </template>
   ```

✅ **输出结果：** 页面显示两个股票卡片组件。

------

### 📚 金融学习： ###

- 学习“道琼斯指数”“上证指数”含义。
- 理解“指数 ≠ 单个股票”的区别。
- 任务：找出3个你熟悉的上市公司代码（比如腾讯、阿里、苹果）。

------

## 📅 Day 4：Axios 请求与假数据 ##

**目标：** 学习如何让 Vue 调用接口。

### 🧩 技术任务： ###

1. 安装 Axios：

   ```bash
   npm install axios
   ```

2. 在 `App.vue` 中模拟调用（先用假数据接口）：

   ```vue
   <script setup>
   import axios from 'axios'
   import { ref, onMounted } from 'vue'
   
   const stockData = ref([])
   
   onMounted(async () => {
     const res = await axios.get('https://mocki.io/v1/6f4c4b58-d0db-4e49-a3b2-cc7925d3b12a')
     stockData.value = res.data
   })
   </script>
   
   <template>
     <div v-for="s in stockData" :key="s.code">
       <p>{{ s.name }} - {{ s.price }}</p>
     </div>
   </template>
   ```

✅ **输出结果：** 页面加载远程假数据并显示。

------

### 📚 金融学习： ###

- 学习“财报指标”（市盈率PE、市值、营收）。
- 推荐阅读：《雪球网》热门文章（搜索“市盈率 是什么”）
- 任务：写一段简短理解（50字）解释什么是市盈率。

------

## 📅 Day 5：ECharts 可视化初步 ##

**目标：** 能在页面展示一张股票价格折线图。

### 🧩 技术任务： ###

1. 安装 ECharts：

   ```bash
   npm install echarts
   ```

2. 新建组件 `src/components/StockChart.vue`

   ```vue
   <template>
     <div ref="chart" style="width: 600px; height: 400px;"></div>
   </template>
   
   <script setup>
   import * as echarts from 'echarts'
   import { onMounted, ref } from 'vue'
   
   const chart = ref(null)
   
   onMounted(() => {
     const myChart = echarts.init(chart.value)
     const option = {
       title: { text: 'AAPL 股票价格走势' },
       xAxis: { data: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri'] },
       yAxis: {},
       series: [{ type: 'line', data: [182, 185, 184, 188, 190] }]
     }
     myChart.setOption(option)
   })
   </script>
   ```

✅ **输出结果：** 页面上出现一张折线图。

------

### 📚 金融学习： ###

- 学习股票趋势线的意义。
- 了解技术分析 vs 基本面分析。
- 任务：尝试解释图中“上升趋势”代表什么。

------

## 📅 Day 6-7：复习 + 页面整合 + 金融复盘 ##

**目标：** 把前几天的组件整合成一个“AI理财首页”。

### 🧩 技术任务： ###

1. 整合组件：
   - 首页顶部展示项目名；
   - 中间显示两个 `StockCard`；
   - 下方嵌入 `StockChart`；
   - 所有样式简单排版（用 Flex 布局或 Tailwind）。
2. 提交到 GitHub：
   - 打开 GitHub Desktop；
   - 点击 **Commit to main → Push origin**；
   - 检查网页端同步成功。

✅ **输出结果：**
 项目首页完整、能显示股票信息与折线图。

------

### 📚 金融学习： ###

- 回顾本周内容；
- 阅读《经济学人》或财联社“每日简报”；
- 写一篇 100 字周总结：
  - 本周学了什么？
  - 看到哪些真实股票波动？

------

## 🎯 第二周结束后你将： ##

✅ 能运行并修改 Vue 项目；
 ✅ 理解前端组件、数据流与 ECharts 使用；
 ✅ 掌握基础股票知识（K线、指标、指数含义）；
 ✅ GitHub 有第一次完整提交。

------

要不要我帮你直接生成这个「第二周任务表」的 Markdown 文件？
 可以直接放进你的 GitHub 项目 `/docs/week2.md` 里做进度记录。