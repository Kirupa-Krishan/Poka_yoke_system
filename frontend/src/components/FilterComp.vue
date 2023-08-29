<template>
  <div>
    <b-card-group columns class="crud">
      <b-card header-tag="header" footer-tag="footer" class="crud-item">
        <template #header>
          <h6 class="mb-0">Get All Logs</h6>
        </template>
        <b-button @click="getLogs" block variant="primary">Get All</b-button>
      </b-card>
      <b-card header-tag="header" footer-tag="footer" class="crud-item">
        <template #header>
          <h6 class="mb-0">Filter Employee</h6>
        </template>
        <b-input-group>
          <b-form-select
            id="Filter-input"
            v-model="filter"
            :options="FilterOptions"
            required
          ></b-form-select>
        <b-input-group-append>
          <b-button @click="filterSearch" size="sm" class="my-2 my-sm-0" type="submit">Search</b-button>
        </b-input-group-append>
        </b-input-group>
      </b-card>
    </b-card-group>
  </div>
</template>

<script>
export default {
  data(){
    return{
      filter:null,
      FilterOptions:[
        { value: null, text: "Please select Filter Type" },
        { value: "Added employee", text: "Insert" },
        { value: "Updated employee", text: "Update" },
        { value: "Deleted employee", text: "Delete" },
        { value: "Logged in", text: "Login" },
      ],
    }
  },
  methods: {
     getLogs(){
      this.$emit('update-log','all')      
    },
    filterSearch(){
      this.$emit('update-log',this.filter)
    }
  },
};
</script>
    <style scoped>
.crud {
  display: flex;
  flex-direction: column;
  justify-content: space-evenly;
}
.crud-item {
  max-width: 100%;
}
</style>