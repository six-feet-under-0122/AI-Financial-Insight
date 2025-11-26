<script>
import StockChart from './StockChart.vue';
import axios from 'axios';
export default {
    name: 'StockCard',
    data() {
        return {
            stockName: 'six_feet_under',
            stockCode: 'SFU',
            stockPrice: 100,
            stockStatus: 'up', // 'up' | 'down' | 'flat'
            some_methods: '01.22'
        }
    },
    computed: {
        // 用于 :class 绑定，返回对象（推荐）
        //this指向当前组件实例（事件？）
        priceClass() {
            return {
                up: this.stockStatus === 'up',
                down: this.stockStatus === 'down',
                flat: this.stockStatus === 'flat'
            }
        },
        statusSymbol() {
            if (this.stockStatus === 'up') return '▲'
            if (this.stockStatus === 'down') return '▼'
            return '—'
        },
        status(){
            return {
                up: this.stockStatus === 'up',
                down: this.stockStatus === 'down',
                flat: this.stockStatus === 'flat'
            }
            
        }
    },
    methods: {
        toggleStatus() {
            if (this.stockStatus === 'up') this.stockStatus = 'down'
            else if (this.stockStatus === 'down') this.stockStatus = 'flat'
            else this.stockStatus = 'up'
        },
        toggleup(){
            console.log("up")
            this.stockPrice+=1

        },
        toggledown(){
            console.log("down")
            this.stockPrice-=1

        },
        async update_code_name(){
            try{
            const response = await axios.get('http://localhost:5000/api/code_name')
            this.stockCode=response.data.code_name
            console.log("code_name:"+this.stockCode)
            }
            catch(error){
                this.stockCode="error"+" "+error.message
                console.log("error"+error.message)
            }
        }

    },
    components: {
        StockChart
    }
}
</script>


<template>
    <div class="stock-card" style="width:100%">
        <header class="card-header">
            <div class="title">name:{{ stockName }}</div>
            <div class="code">
                code:{{ stockCode }}
                <button @click="update_code_name">update</button>
            </div>
            <div class="price">price:{{ stockPrice }}
                <button @click="toggleup" >+</button>
                <button @click="toggledown">-</button>
            </div>

            <div>status:<span :class="status">{{ stockStatus }}</span></div>
            <StockChart :something="some_methods" :codeName="stockCode"/>
        </header>
    </div>
</template>

<style scoped>
.stock-card{
    width: 300px;
    border-radius: 10px;
    padding: 14px;
    box-shadow: 0 6px 18px rgba(0,0,0,0.06);
    background: #ffffff;
    border: 1px solid #eef2f7;
    display:flex;
    flex-direction:row;
    gap:12px;
}
button{
    width:auto;
    text-align: center;
    background-color:black;
    border:none;
    border-radius: 12px 5px 5px;
    color: white;
}
.price{
    display:flex;
    flex-direction:row;
    gap:5px;/* 项目之间间距 */
}
.text{
    color:rgba(125, 125, 125, 0.06)
}

.up{
    color:red;
}
.down{
    color:green;
}

</style>

