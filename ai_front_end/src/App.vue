<script setup>
import{ref}from 'vue';
import axios from 'axios';  
const keywords = ref('');
const result = ref('');
const loading = ref(false);
const search_name = async()=>{
    loading.value = true;
    try{
        const res = await axios.get("/api",
            {
                params: {
                    keywords: keywords.value
                }
            }
        )
        result.value = res.data.msg
    }catch(error){
        console.error("Error fetching data:", error);
    }finally{
        loading.value = false;
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
<div v-if="loading">loading...</div>
<div v-else>{{ result }}</div>
</template>


<style scoped>


</style>

