<template>
  <div class="hello">
    <table>
      <thead>
       <tr>
        <th>Vendor</th>
        <th>Model</th>
        <th>Year</th>
        <th>Volume</th>
       </tr>
      </thead>
      <tbody>
        <tr v-for='(car, i) in cars' :key='i'>
          <td>{{ car.vendor }}</td>
          <td>{{ car.model }}</td>
          <td>{{ car.year }}</td>
          <td>{{ car.volume }}</td>
        </tr>
      </tbody>
    </table>
    <div class="users">
    <table>
      <thead>
       <tr>
        <th>Username</th>
       </tr>
      </thead>
      <tbody>
        <tr v-for='(usr, x) in users' :key='x'>
          <td>{{ usr.username }}</td>
        </tr>
      </tbody>
    </table>
  </div>
  </div>

</template>

<script>
export default {
  name: 'HelloWorld',
  data() {
    return {
      cars: null,
      users: null,
    };
  },
  created(){
    this.getCars()
    this.getUsers()
  },
  methods: {
  getCars () {
    fetch("http://127.0.0.1:8000/api/cars/")
    .then(response => response.json())
    .then((res) => {
      this.cars = res;

      })
    },
  getUsers () {
    fetch("http://127.0.0.1:8000/api/users/")
    .then(response => response.json())
    .then((res) => {
      this.users = res;

    })
  }
}

};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
