<script setup>
import{ref}from 'vue';
import axios from 'axios';  
const keywords = ref('');
const result = ref('');
const search_name = async()=>{
    try{
        const res = await axios.get("/api")
        result.value = res.data.msg
    }catch(error){
        console.error("Error fetching data:", error);
    }
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

</template>


<style scoped>


</style>

