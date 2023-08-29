<template>
  <div>
    <b-card-group columns class="crud">
      <b-card header-tag="header" footer-tag="footer" class="crud-item">
        <template #header>
          <h6 class="mb-0">Add Employee</h6>
        </template>
        <b-button v-b-modal.add-emp block variant="success">Add</b-button>
      </b-card>
      <b-card header-tag="header" footer-tag="footer" class="crud-item">
        <template #header>
          <h6 class="mb-0">Update Employee</h6>
        </template>
        <b-button v-b-modal.edit-emp block variant="primary">Update</b-button>
      </b-card>
      <b-card header-tag="header" footer-tag="footer" class="crud-item">
        <template #header>
          <h6 class="mb-0">Delete Employee</h6>
        </template>
        <b-button v-b-modal.delete-emp block variant="danger">Delete</b-button>
      </b-card>
    </b-card-group>
    <b-modal
      id="add-emp"
      ref="modal"
      title="Add Employee"
      @show="resetModal"
      @hidden="resetModal"
      @ok="handleOk"
    >
      <form ref="form" @submit.stop.prevent="handleSubmit">
        <b-form-group
          label="Name"
          label-for="name-input"
          invalid-feedback="Name is required"
          :state="nameState"
        >
          <b-form-input
            id="name-input"
            v-model="employee.name"
            :state="nameState"
            required
          ></b-form-input>
        </b-form-group>
        <b-form-group label="Position" label-for="position-input">
          <b-form-select
            id="position-input"
            v-model="employee.position"
            :options="Positionoptions"
            required
          ></b-form-select>
        </b-form-group>
        <b-form-group label="Password" label-for="pass-input">
          <b-form-input
            id="pass-input"
            v-model="employee.password"
            required
          ></b-form-input>
        </b-form-group>
        <b-form-group label="Status" label-for="status-input">
          <b-form-select
            id="status-input"
            v-model="employee.status"
            :options="Statusoptions"
            required
          ></b-form-select>
        </b-form-group>
      </form>
    </b-modal>
    <b-modal
      id="edit-emp"
      ref="modal"
      title="Enter Employee ID"
      @shown="resetEditModal"
      @hidden="resetModal"
    >
      <template #modal-footer>
        <b-button
          size="sm"
          variant="primary"
          v-if="toggleGetEditState"
          @click="getEmployee"
        >
          Get Details
        </b-button>
        <b-button
          size="sm"
          variant="primary"
          v-else
          @click="updateEmployee"
        >
          Update Details
        </b-button>
      </template>
      <form ref="form" @submit.stop.prevent="handleSubmit">
        <b-form-group id="eid-input" label="Enter Employee ID" label-for="eid">
          <b-form-input id="eid" v-model="employee.id" trim></b-form-input>
        </b-form-group>

        <b-form-group
          id="ename-input"
          label="Enter Employee Name"
          label-for="ename"
          :invalid-feedback="enameinvalidFeedback"
          :state="enamestate"
          v-if="!toggleGetEditState"
        >
          <b-form-input
            id="ename"
            v-model="employee.name"
            :state="enamestate"
            trim
          ></b-form-input>
        </b-form-group>
        <b-form-group
          id="eposition-input"
          label="Enter Employee Position"
          label-for="eposition"
          :invalid-feedback="epositioninvalidFeedback"
          :state="epositionstate"
          v-if="!toggleGetEditState"
        >
        <b-form-select
            id="position-input"
            v-model="employee.position"
            :options="Positionoptions"
            required
          ></b-form-select>
        </b-form-group>
        <b-form-group
          id="epassword-input"
          label="Enter Employee Password"
          label-for="epass"
          :invalid-feedback="vcapacityinvalidFeedback"
          :state="epasswordState"
          v-if="!toggleGetEditState"
        >
          <b-form-input
            id="epass"
            v-model="employee.password"
            :state="epasswordState"
            trim
          ></b-form-input>
        </b-form-group>
        <b-form-group label="Status" label-for="status-input"
        v-if="!toggleGetEditState">
          <b-form-select
            id="status-input"
            v-model="employee.status"
            :options="Statusoptions"
            required
          ></b-form-select>
        </b-form-group>
        
      </form>
    </b-modal>
    <b-modal
      id="delete-emp"
      ref="modal"
      title="Delete Employee"
      @show="resetModal"
      @hidden="resetModal"
      @ok="deleteEmpDetails"
    >
      <form ref="form" @submit.stop.prevent="handleSubmit">
        <b-form-group id="eid-input" label="Enter Employee ID" label-for="eid">
          <b-form-input
            id="eid"
            v-model="employee.id"
            trim
            required
          ></b-form-input>
        </b-form-group>
      </form>
    </b-modal>
  </div>
</template>

<script>
import axios from "axios";
export default {
  data() {
    return {
      employee: {
        id: null,
        name: "",
        position: null,
        password: "",
        status: null,
      },
      nameState: null,
      Positionoptions: [
        { value: null, text: "Please select Empplyee Status" },
        { value: "Intern", text: "Intern" },
        { value: "Trainee", text: "Trainee" },
        { value: "Team Lead", text: "Team Lead" },
        { value: "Manager", text: "Manager" },
      ],
      Statusoptions: [
        { value: null, text: "Please select Empplyee Status" },
        { value: true, text: "Valid" },
        { value: false, text: "Invalid" },
      ],
      toggleGetEditState: true,
    };
  },
  methods: {
    checkFormValidity() {
      const valid = this.$refs.form.checkValidity();
      this.nameState = valid;
      return valid;
    },
    toggleGetEdit(){
      this.toggleGetEditState = !this.toggleGetEditState
  },
    resetModal() {
      (this.employee.id = null),
        (this.employee.name = ""),
        (this.employee.position = ""),
        (this.employee.password = ""),
        (this.employee.status = false);
    },
    resetEditModal() {
      (this.toggleGetEditState = true),
        (this.employee.id = null),
        (this.employee.name = ""),
        (this.employee.position = ""),
        (this.employee.password = ""),
        (this.employee.status = false);
    },
    handleOk(bvModalEvent) {
      // Prevent modal from closing
      bvModalEvent.preventDefault();
      // Trigger submit handler
      this.handleSubmit();
    },
   async handleSubmit() {
      await axios.post("http://127.0.0.1:5000/add_employee", this.employee);
      // Hide the modal manually
      this.$nextTick(() => {
        alert("Employee Added");
        this.$bvModal.hide("add-emp");
      });
      this.$emit('update-log','all') 
    },
    async getEmployee(bvModalEvent) {
      bvModalEvent.preventDefault();
      // Exit when the form isn't valid
      await axios
        .get(
          `http://127.0.0.1:5000/get_employee/${this.employee.id}`
          // {headers: { 'x-access-token': localStorage.getItem('token') }}
        )
        .then((res) => {
          (this.employee.id = res.data["_id"]),
            (this.employee.name = res.data["name"]),
            (this.employee.position = res.data["position"]),
            (this.employee.password = res.data["password"]),
            (this.employee.status = res.data["status"]);
          this.toggleGetEdit();
        })
        .catch((err) => console.log(err));
    },
    async updateEmployee(bvModalEvent) {
      this.toggleGetEdit();
      bvModalEvent.preventDefault();
      // Exit when the form isn't valid
      await axios
        .put(
          `http://127.0.0.1:5000/update_employee/${this.employee.id}`,
          {
            "_id": this.employee.id,
            "name": this.employee.name,
            "position": this.employee.position,
            "password": this.employee.password,
            "status": this.employee.status,
          },
          {
            headers: { "x-access-token": localStorage.getItem("token") },
          }
        )
        .then(() => {
          this.$bvModal.msgBoxOk("Data Was Updated Successfully", {
            title: "Confirmation",
            size: "sm",
            buttonSize: "sm",
            okVariant: "success",
            headerClass: "p-2 border-bottom-0",
            footerClass: "p-2 border-top-0",
            centered: true,
          });
        })
        .catch((err) => console.log(err));
      this.resetModal();
      this.$bvModal.hide("edit-emp");
      this.$emit('update-log','all') 
    },
    deleteEmpDetails(bvModalEvent) {
      bvModalEvent.preventDefault();
      this.$bvModal
        .msgBoxConfirm("Please confirm that you want to delete everything.", {
          title: "Please Confirm",
          size: "sm",
          buttonSize: "sm",
          okVariant: "danger",
          okTitle: "YES",
          cancelTitle: "NO",
          footerClass: "p-2",
          hideHeaderClose: false,
          centered: true,
        })
        .then(async (res) => {
          if (res) {
            await axios
              .delete(
                `http://127.0.0.1:5000/delete_employee/${this.employee.id}`
                //{headers: { 'x-access-token': localStorage.getItem('token') } }
              )
              .then(() => {
                this.$bvModal.msgBoxOk("Data Was Deleted Successfully", {
                  title: "Confirmation",
                  size: "sm",
                  buttonSize: "sm",
                  okVariant: "success",
                  headerClass: "p-2 border-bottom-0",
                  footerClass: "p-2 border-top-0",
                  centered: true,
                });
              });
          }
          this.resetModal();
          this.$bvModal.hide("delete-emp");
          this.$emit('update-log','all') 
        })
        .catch((err) => {
          console.log(err);
        });
    },
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