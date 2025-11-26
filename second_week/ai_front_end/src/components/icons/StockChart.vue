<script>
//局部使用vue-echarts？？
import {ref}from 'vue'
import {use}from 'echarts/core'
import { CanvasRenderer } from 'echarts/renderers'
import {LineChart } from 'echarts/charts'
import {TitleComponent,TooltipComponent,GridComponent,LegendComponent} from 'echarts/components'
use([CanvasRenderer,LineChart,TitleComponent,TooltipComponent,GridComponent,LegendComponent])
export default {
    name:'stockChart',
    props:["something",'price','stockStatus','codeName'],
    data(){
        return {
            //echarts的option
            chartoption:{
                title:{
                    text:'sample: six_feet_under stock chart',
                    subtext:this.something
                },
                tooltip:{
                    trigger:'axis'

                },
                legend:{
                    data:[this.codeName]

                },
                xAxis:{
                    type:'category',
                   data:['9:00','10:00','11:00','12:00','13:00','14:00','15:00']
                 },
                yAxis:{
                    type:'value'
                },                
                series:[{
                    name:this.codeName,//与legend配对；
                    type:'line',
                    data:[99,100,101,102,101,100,100]
                }]
            }
        }
    },
    methods:{
        //更改图表数据
        //array.from()方法用于从类似数组或可迭代对象创建一个新的数组实例。
        updateChartData(){
            const newData=Array.from({length:7},()=>Math.floor(Math.random()*10)+95);
            this.chartoption.series[0].data=newData;
        }
    },
    mounted(){
        console.log("StockChart mounted")
        console.log(this.$refs.chart)
    }
}
</script>



<template>
<div style="width:500px;height: 400px;">
    <!-- 一定要有大小。。。。 -->
    <div>
        <button @click="updateChartData">Update Chart Data</button>
    </div>
    <v-chart :option="chartoption" ref="chart" :autoresize="true" class="stock_chart"></v-chart>
    
</div>
<div class="test">{{ something }}</div>


</template>

<style>
.test {
color:brown;
}


</style>