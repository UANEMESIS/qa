<template>
  <div class="form-file">
    <input id="image-file" type="file"/>
    <button v-on:click="myFunc()">Send</button>
  </div>
</template>

<script>
export default {
  name: 'Fileform',
  props: {},
  methods: {
   myFunc() {
     let fileInput = document.querySelector("input[type='file']").files[0];
     let data = {"file": fileInput}
     let formData = new FormData();

     for(let name in data) {
      formData.append(name, data[name])
     }

     let options = {
     method: 'POST',
     body: formData,
     }

     fetch('http://127.0.0.1:8000/api/upload/', options)
     .then(res => {
      if (res.ok) {
        void(0) //window.location.replace("/workshops/")
      } else {
        void(0)

      }
     })
    .catch((err) => console.log(err));
   }
  }
  


}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>
