<!-- eslint-disable vue/multi-word-component-names -->
<template>
    <div class="login" v-if="ShowLogin">
      <div class="left-section">
        <h1 class="title">"Can Sheng" Advanced Driver Assistance</h1>
        <div class="brief-container">
          <div class="brief">
            <p>Brief Introduction</p>
          </div>
        <div class="expanded-brief">
          <p>"参乘(Can Sheng)", an ancient Chinese word, is interpreted as a person who accompanies or rides with a passenger. In ancient times, 
            when travelling in a car, the honorable person was on the left, the imperialist was in the middle, and one person sat with him 
            on the right.</p>
          <p>"Can Sheng" Advanced Driver Assistance intelligently analyzes your fatigue status as well as your identity through a variety of sensors,
            using computer vision, cloud computing and other technologies. "Can Sheng" brings you fatigue detection, face recognition and other features
              to keep you safe on the road.</p>  
        </div>
      </div>
    
      </div>
        <div class="right-section">
          <div class="split-line"></div>
            <h1 class="title">Account</h1>
          <div class="boxform">

          <div class="item">
            <input type="text" placeholder="userID" id="user_name" name="user_name" required="required" v-model="LoginName">
          </div>

          <div class="item">
            <input type="password" placeholder="user password" id="user_key" name="user_key" required="required" v-model="LoginKey">
          </div>

          <a class = "button1" @click="Login">
            <input type="submit" value="login" id="user_submit"/>
          </a>

          <a class = "button2" @click="Register">
            <input type="submit" value="register" id="user_submit"/>
          </a>
        </div>

        <div class="messagebox" v-if="messageFlag">
          {{ notice }}
        </div>
      </div>
    </div>


</template>
  

  <script>
  import axios from 'axios';
   
  export default {
    // eslint-disable-next-line vue/multi-word-component-names
    name: 'Login',
    data() {
      return {
        ShowLogin: true,
        messageFlag: false,
        username: '',
        password: '',
        notice: ''
      }
    },
    methods: {
      showMessage(text) {
        this.notice = text;
        this.messageFlag = true;
        setTimeout(() => {
            this.messageFlag = false;
        }, 2000);
      },
      Login() {
        const username = this.LoginName
        const password = this.LoginKey
        console.log(username)
        var that = this
        axios.get('http://127.0.0.1:5000/user', {
          headers: {
            'Access-Control-Allow-Origin': '*'
          }
        })
        .then(response => {
          console.log(response.data);
          let user = response.data.find(u => u.username === username);
          if(user && user.password === password){
            console.log('success');
            that.showMessage('登录成功');
            //that.ShowLogin = false;
          }
          else if(user && user.password != password){
            that.showMessage('密码错误');
          }
          else{
            console.log('fail');
            that.showMessage('用户名不存在!');
          }
        })
        .catch(error => {
          console.error(error);
          console.log('error');
        });
      },

      Register(){
        const username = this.LoginName
        const password = this.LoginKey

        console.log(username)
        var that = this

        axios.post('http://127.0.0.1:5000/register', {
          username,
          password,
          headers: {
            'Access-Control-Allow-Origin': '*'
          }
        })
        .then(response => {
          //that.showMessage(response.data.message)
          console.log('success')
          console.log(response.data.message)
          that.showMessage('注册成功')
        }).catch(error => {
          that.showMessage(error.response.data.message)
        //this.message = error.response.data.message;
        });
      
      }
   
    }
  }
  </script>
  
<style>
.login {
  position: absolute;
  top: 60%;
  left: 50%;
  transform: translate(-50%, -50%);
  width: 70%;
  height: 50%;
  padding-top: 20px;
  padding-bottom: 20px;
  background: rgba(255, 255, 255, 0.864);
  z-index: 2000;
  overflow: auto;
  text-align: center;
  border-radius: 20px;
  display: flex;
}

.left-section {
  position: relative;
  width: 70%;
  height: 50%;
  padding: 20px;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  cursor: pointer;
}

.left-section .title {
  position: absolute;
  top: 0%;
  font-size: 35px;
  letter-spacing: 2px;
  font-family: Alice;
  color: #ff8400;
}

.left-section .brief-container {
  position: absolute;
  left: 5%;
  top: 20%;
  margin-top: 15px;
  align-items: flex-start; 
  width: 100%; /* Set the width to 100% to fill the left-section */
}

.left-section .brief {
  position: absolute;
  cursor: pointer;
  font-size: 20px;
  letter-spacing: 2px;
  font-family: Alice;
  color: #000000;
  margin-top: 15px;
}



.left-section .expanded-brief {
  position: absolute;
  display: none;
  padding: 10px;
  font-size: 20px;
  margin-top: 30px;
  width: 86%;
  align-items: flex-start; 
  font-family: Alice;
  color: #000000;
  left: 0%; /* Align the expanded-brief to the left */
  top: calc(50% + 10px); /* Calculate 10px below the brief */
  display: block;
}


.right-section {
  width: 20%;
  height: 80%;
  padding: 20px;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}

.right-section .split-line {
  position: absolute;
  top: 15%;
  left: 73%; /* Place the line at 70% of the right-section's width */
  height: 70%;
  width: 2px;
  background-color: #000;
  z-index: 1;
}

.right-section .title {
  font-size: 35px;
  letter-spacing: 2px;
  font-family: Alice;
  color: #ff8400;
}

.login .boxform {
  margin-top: 15px;
}

.boxform .item {
  margin-top: 15px;
}

.boxform .item input {
  width: 80%;
  font-size: 20px;
  font-family: Alice;
  border: 0;
  border-bottom: 2px solid #000;
  padding: 5px 10px;
  background: #ffffff00;
  color: #000;
}


.boxform .item input::placeholder {
  color: #00000099;
}

.login .boxform .button1 input {
  margin: 0px auto;
  margin-top: 50px;
  margin-left: 0px; 
  width: 120px;
  height: 40px;
  font-size: 25px;
  font-weight: 600;
  font-family: Alice;
  border: 0;
  background-color: rgb(255, 255, 255, 0.5);
  box-shadow: 4px 4px 8px rgba(0, 0, 0, 0.2),
    -4px -4px 8px rgba(255, 255, 255, 0.5);
  border-radius: 20px;
  transition: box-shadow 0.2s ease-out;
  position: relative;
  margin-bottom: 15px;
}

.login .boxform .button2 input {
  margin: 0px auto;
  margin-top: 10px;
  margin-left: 0px; 
  width: 120px;
  height: 40px;
  font-size: 25px;
  font-weight: 600;
  font-family: Alice;
  border: 0;
  background-color: rgb(255, 255, 255, 0.5);
  box-shadow: 4px 4px 8px rgba(0, 0, 0, 0.2),
    -4px -4px 8px rgba(255, 255, 255, 0.5);
  border-radius: 20px;
  transition: box-shadow 0.2s ease-out;
  position: relative;
}

.login .box_orm .button1 input:hover {
  box-shadow: 0px 0px 0px rgba(0, 0, 0, 0.2),
    0px 0px 0px rgba(255, 255, 255, 0.1), inset 4px 4px 4px rgba(0, 0, 0, 0.1),
    inset -4px -4px 4px rgba(255, 255, 255, 1);
  transition: box-shadow 0.2s ease-out;
  cursor: pointer;
}

.login .box_orm .button2 input:hover {
  box-shadow: 0px 0px 0px rgba(0, 0, 0, 0.2),
    0px 0px 0px rgba(255, 255, 255, 0.1), inset 4px 4px 4px rgba(0, 0, 0, 0.1),
    inset -4px -4px 4px rgba(255, 255, 255, 1);
  transition: box-shadow 0.2s ease-out;
  cursor: pointer;
}

.messagebox {
  background: rgb(255, 255, 255);
  border-radius: 20px;
  color: #000000;
  position: absolute;
  padding: 25px 30px;
  left: 50%;
  width: 200px;
  transform: translate(-50%, -50%);
  top: 50%;
  text-align: center;
  font-size: 20px;
}
</style>