<!-- eslint-disable vue/multi-word-component-names -->
<template>
    <div class="about">
        <div class="brief-container">
          <div class="brief">
            <p>About</p>
          </div>
        <div class="expanded-brief">
          <p>This project was completed at the School of Computing, NUS, under the supervision of Professor
             TAN Wee Kek, with a team of five members, including Wang Weibo, Lin Wuzhen, Qiu Tian, Sun yanshu, Zhang jingyuan. 
             The project took 3 weeks to complete. Please ask the person in charge for detailed technical requirements. </p>
          <p>The project code has been posted on github https://github.com/AioT-Tansome/sakura.</p>  
          <p>Project contact phone number: +8618069570895</p>  
          <p>Project contact QQ: 3111219797</p>  
          <p>Project Contact Address: Shanghai Jiaotong University Minhang Campus</p>  
        </div>
    </div>
</div>

</template>
  

  <script>
   
  export default {
    // eslint-disable-next-line vue/multi-word-component-names

  }
  </script>
  
<style>
.about {
  position: absolute;
  top: 60%;
  left: 50%;
  transform: translate(-50%, -50%);
  width: 80%;
  height: 60%;
  padding-top: 20px;
  padding-bottom: 20px;
  background: rgba(255, 255, 255, 0.864);
  z-index: 2000;
  overflow: auto;
  text-align: center;
  border-radius: 20px;
  display: flex;
}



.about .brief-container {
  position: absolute;
  left: 5%;
  top: 5%;
  margin-top: 0px;
  align-items: flex-start; 
  width: 100%; /* Set the width to 100% to fill the left-section */
}

.about .brief {
  position: absolute;
  cursor: pointer;
  font-size: 20px;
  letter-spacing: 2px;
  font-family: mvboli;
  color: #000000;
  margin-top: 15px;
}



.about .expanded-brief {
  position: absolute;
  display: none;
  padding: 10px;
  font-size: 20px;
  margin-top: 30px;
  width: 90%;
  align-items: flex-start; 
  font-family: mvboli;
  color: #000000;
  left: 0%; /* Align the expanded-brief to the left */
  top: calc(50% + 10px); /* Calculate 10px below the brief */
  display: block;
}



</style>