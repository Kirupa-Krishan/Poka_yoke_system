<template>
    <div>
    <b-card id="card">
      <b-form @submit="submitForm">
        <div class="text-center">
          <b-img src="https://cdn.pixabay.com/photo/2016/03/31/19/56/avatar-1295397__340.png"
            fluid alt="profile" class="img-thumbnail rounded-circle my-3" width="200px"></b-img>
        </div>
        <b-form-group id="Username" label="User Name">
          <b-form-input v-model="username" placeholder="User Name"></b-form-input>
        </b-form-group>
        <b-form-group id="password" label="Password">
          <b-form-input type="password" v-model="password" placeholder="Password"></b-form-input>
        </b-form-group>
        <div class="text-center">
          <b-button type="submit" variant="primary" class="mb-5 w-100">Login</b-button>
        </div>
      </b-form>
    </b-card>
</div>
</template>

<script>
export default {
data() {
return {
  username: '',
  password: ''
};
},
methods: {
submitForm(event) {
  event.preventDefault();
  // Handle form submission logic here
}
}
};
</script>
<style scoped>
#card{
margin:60px 450px;
align-content: center;
}

.btn-color{
background-color: #0e1c36;
color: #fff;

}
.profile-image-pic{
height: 200px;
width: 200px;
object-fit: cover;
}

.cardbody-color{
background-color: #ebf2fa;
}

a{
text-decoration: none;
}
</style>