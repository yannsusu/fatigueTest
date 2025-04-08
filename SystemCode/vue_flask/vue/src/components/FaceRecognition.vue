<template>
    <div class="container">
      <div class="Box"></div>
        <img :src="latest_image_url" alt="Latest Image">
      <div class="square"></div>  
    </div>  
  </template>
  
<script>
export default {
  data() {
    return {
      latest_image_url: '' // The URL of the most recent image
    };
  },
  mounted() {
    // Retrieve the URL of the most recent image from the Flask endpoint
    this.getLatestImageUrl();
  },
  methods: {
    getLatestImageUrl() {
      const url = 'http://localhost:5000/video';
      fetch(url)
        .then(response => {
          if (!response.ok) {
            throw new Error(`HTTP error ${response.status}`);
          }
          console.log('success')
          return response.blob();
        })
        .then(blob => {
          this.latest_image_url = URL.createObjectURL(blob);
        })
        .catch(error => {
          console.error(error);
        });
    }
  }
};
</script>

  <style>
  .container {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 80%;
  }

  .Box {
    position: relative;
    top:10%;
    left:58%;
    width: 300px;
    height: 500px;
    padding: 10px;
    background-color: rgba(255, 255, 255, 0.777); 
    border-radius: 8px;
    /* background-image: url('@/assets/asuna.png'); */
    background-size: cover;
    opacity: 0.5;
  }

  .square {
    position: relative;
    top:10%;
    right:30%;
    width:55%;
    height: 500px;

    border: 1px solid ;
    padding: 10px;
    border-radius: 8px;
    background-color: rgba(255, 255, 255, 0.858); 
    /* background-image: url('@/assets/asuna.png'); */
    background-size: cover;
    opacity: 0.5;
    /* background-color: #f0f0f0; */
  }
  </style>
  