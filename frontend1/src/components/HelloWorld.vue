<template>
  <div class="hello">
    <div>
    <h1>{{ msg }}</h1>
    <h2>I am working to combine Vue with Django</h2>
    </div>

    <div><span class="glyphicon glyphicon-magnet"></span>
    <table class="table">
    <thead class="thead-dark">
    <tr>
        <th scope="col">Serial</th>
        <th scope="col">First Name</th>
      <th scope="col">Last Name</th>
      <th scope="col">Handle</th>
      <th scope="col">action</th>
       <th><input type="search" class="form-control rounded" placeholder="Search" aria-label="Search"  /></th>
    </tr>
   </thead>
   <tbody>
     <tr>
      <th scope="row">1</th>
      <td>Mark</td>
      <td>Otto</td>
      <td>@mdo</td>
      <td><button class="btn btn-danger">Delete</button></td>
    </tr>
     <tr>
      <th scope="row">1</th>
      <td>Mark</td>
      <td>Otto</td>
      <td>@mdo</td>
      <td><button class="btn btn-danger">Delete</button></td>
    </tr>
     <tr>
      <th scope="row">1</th>
      <td>Mark</td>
      <td>Otto</td>
      <td>@mdo</td>
      <td><button class="btn btn-danger">Delete</button></td>
    </tr>
     <tr>
      <th scope="row">1</th>
      <td>Mark</td>
      <td>Otto</td>
      <td>@mdo</td>
      <td><button class="btn btn-danger">Delete</button></td>
    </tr>
     <tr>
      <th scope="row">1</th>
      <td>Mark</td>
      <td>Otto</td>
      <td>@mdo</td>
      <td><button class="btn btn-danger">Delete</button></td>
    </tr>
   </tbody>
   </table>
   </div>
   <button class="btn btn-success">Submit</button>
  </div>
</template>

<script>
export default {
  name: 'HelloWorld',
  data () {
    return {
      msg: 'Welcome to My Vue.js App'
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h1, h2 {
  font-weight: normal;
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
