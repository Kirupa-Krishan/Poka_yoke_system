<template>
    <div>
      <b-textarea id="textarea-plaintext" plaintext :value="text" rows="23" max-rows="23" no-resize></b-textarea>
    </div>
  </template>
  
  <script>
  // import axios from 'axios';
    export default {
      props:['logs','emp'],
      data() {
        return {
          text:''
        }
      },
mounted(){
  for(let x in this.logs){
    console.log(this.logs[x])
    this.text = this.text+this.logs[x].at+" : "+this.logs[x].action+" "+this.logs[x].name+'\n'
  }
}

    }
  </script>

<style scoped>
#textarea-plaintext{
    background-color: white;
    border-radius: 5px;
    padding:10px;
}
</style>