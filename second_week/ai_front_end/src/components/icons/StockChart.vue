<script>
import {ref}from 'vue'
import {use}from 'echarts/renderers'
import { CanvasRenderer } from 'echarts/renderers'
import {LineChart } from 'echarts/charts'
import {TitleComponent,TooltipComponent,GridComponent,LegendComponent} from 'echarts/components'
use([CanvasRenderer,LineChart,TitleComponent,TooltipComponent,GridComponent,LegendComponent])
export default {
    name:'stockChart',
    data(){
        return {
            //eccharts的option
            chartoption:{
                title:{
                    text:'sample: six_feet_under stock chart',
                    subtext:'01.22'
                },
                tooltip:{
                    trigger:'axis'

                },
                legend:{
                    data:['SFU']

                },
                xAxis:{
                    type:'time',
                    data:['9:00','10:00','11:00','12:00','13:00','14:00','15:00']
                },
                yAxis:{
                    series:[{
                    name:"SFU",//与legend配对；
                    type:'line',
                    data:[99,100,101,102,101,100,100]
                }]
                }


            }
        }
    },
    methods:{
        //更改图表数据
        


    }
}
</script>


<template>
<div>
sss
</div>


</template>

<style>



</style>