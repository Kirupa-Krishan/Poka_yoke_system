<template>
<div>
<NavbarComp/>
<div class="dashboard">
<CrudCompVue @update-log="getLogs" class="item-1"/>
<LogFeedComp :logs="logs" :emp="emp" :key="feedkey" class="item-2"/>
<FilterComp @update-log="getLogs" class="item-3"/>
</div>
</div>
</template>

<script>
import NavbarComp from '@/components/NavbarComp.vue';
import LogFeedComp from '@/components/LogFeedComp.vue';
import CrudCompVue from '@/components/CrudComp.vue'
import FilterComp from '@/components/FilterComp.vue';
import axios from 'axios';
export default{
    components:{
        NavbarComp,
        LogFeedComp,
        CrudCompVue,
        FilterComp
    },
    data(){
        return{
        feedkey:1,
        logs:null,
        emp:null
        }
    },
    methods:{
        updateLogFeed(log,emp){
            this.feedkey++
            this.logs = log
            this.emp = emp
        },
    async getLogs(filter){
      await axios.get(`http://127.0.0.1:5000/get_all?filter=${filter}`).then(
        res => {
        console.log("Here",res.data.logs)
        this.updateLogFeed(res.data.logs,res.data.employees)
        }
      )
      
    },
    }

}
</script>

<style scoped>
.dashboard{
    display: flex;
    gap: 20px;
    margin: 20px 20px
;
}

.item-1{
    align-self:self-start;
}
.item-2{
    align-self: self-start;
    flex-grow: 1;
}
.item-3{
    align-self:self-start;
}
</style>