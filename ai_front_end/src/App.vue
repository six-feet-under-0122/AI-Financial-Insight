<script setup>
import{ref,nextTick}from 'vue';
import axios from 'axios';  
import * as echarts from 'echarts';
const keywords = ref('');
const result = ref('');
const loading = ref(false);
const msg_error = ref("");
const search_name = async()=>{
    loading.value = true;
    try{
        const res = await axios.get("http://127.0.0.1:5000/api/search",
            {
                params: {
                    keywords: keywords.value
                }
            }
            // 拼接URL和参数，axios会自动处理编码和格式化
        )
        result.value = res.data;
    }catch(error){
        console.error("Error fetching data:", error);
    }finally{
        loading.value = false;
    }
    console.log("Search completed");
    console.log(result.value);
    await nextTick();
    
    draw_chart(result.value);
    chart = null;
    }
let chart = null;
const draw_chart = (result) => {
    if(result.total === 0)
    {
        msg_error.value = "No data to display in chart";
        console.log("No data to display in chart");
    
        return
    }
    else{
        msg_error.value = null;
    }
    const dom = document.getElementById('chart');
    if (!chart) {
    chart = echarts.init(dom)
}
    const option = {
        title:{
            text:'Sentiment Distribution',
            left:'center'
        },
        tooltip:{
            trigger:'item'
        },
        legend:{
            bottom: 0 
        },
        series:[
            {
                name:"sentiment",
                type:"pie",
                radius:"50%",
                data:[
                    {value:result.positive, name:'Positive'},
                    {value:result.neutral, name:'Neutral'},
                    {value:result.negative, name:'Negative'}
                ]
            }
        ]
}
     chart.setOption(option);
}
//添加加载状态
</script>
<!-- props套props??heihei... -->
<template>
<div>
    <h1>Hello, AI Financial Insight!</h1>
</div>
<form @submit.prevent="search_name">
    <input v-model="keywords" placeholder="Type the stock name..." /> 
    <button type="submit">Search</button>
</form>
<div v-if="loading">loading...</div>
<div v-else>{{ result }}
    <div v-if = "msg_error">{{ msg_error }}</div>
    <div id="chart" style="width: 600px; height: 400px;"></div>
</div>

</template>


<style scoped>


</style>

