<template>
  <div class="M-Flipper" :class="[flipType, {'go': isFlipping}]">
    <div class="digital front" :class="_textClass(frontTextFromData)"></div>
    <div class="digital back" :class="_textClass(backTextFromData)"></div>
  </div>
</template>

<script>
export default {
  name: 'FlipClock',
  data () {
    return {
      isFlipping: false,
      flipType: 'down',
      frontTextFromData: 0,
      backTextFromData: 1
    }
  },
  props: {
    // front paper text
    frontText: {
      type: [Number, String],
      default: 0
    },
    // back paper text
    backText: {
      type: [Number, String],
      default: 1
    },
    // flipping duration, please be consistent with the CSS animation-duration value.
    // Flip animation duration, consistent with animation-duration set in CSS
    duration: {
      type: Number,
      default: 600
    }
  },
  methods: {
    _textClass (number) {
      return 'number' + number
    },
    _flip (type, front, back) {
      // If it is in a rollover, it is not executed
      if (this.isFlipping) {
        return false
      }
      this.frontTextFromData = front
      this.backTextFromData = back
      // Set the flip direction according to the passed type
      this.flipType = type
      // Set the flip state to true
      this.isFlipping = true
      setTimeout(() => {
        // Set the flip state to false
        this.isFlipping = false
        this.frontTextFromData = back
      }, this.duration)
    },
    // lower flop
    flipDown (front, back) {
      this._flip('down', front, back)
    },
    // upper flop
    flipUp (front, back) {
      this._flip('up', front, back)
    },
    // Setting the front plate text
    setFront (text) {
      this.frontTextFromData = text
    },
    // Setting the back plate text
    setBack (text) {
      this.backTextFromData = text
    }
  },
  created () {
    this.frontTextFromData = this.frontText
    this.backTextFromData = this.backText
  }
}
</script>

<style>
.M-Flipper {
  display: inline-block;
  position: relative;
  width: 45px;
  height: 75px;
  line-height: 75px;
  border: solid 1px #000;
  border-radius: 10px;
  background: #fff;
  font-size: 66px;
  color: #fff;
  box-shadow: 0 0 6px rgba(0, 0, 0, 0.5);
  text-align: center;
  font-family: 'Helvetica Neue';
}

.M-Flipper .digital:before,
.M-Flipper .digital:after {
  content: '';
  position: absolute;
  left: 0;
  right: 0;
  background: #000;
  overflow: hidden;
  box-sizing: border-box;
}

.M-Flipper .digital:before {
  top: 0;
  bottom: 50%;
  border-radius: 10px 10px 0 0;
  border-bottom: solid 1px #666;
}

.M-Flipper .digital:after {
  top: 50%;
  bottom: 0;
  border-radius: 0 0 10px 10px;
  line-height: 0;
}

/*turn down*/
.M-Flipper.down .front:before {
  z-index: 3;
}

.M-Flipper.down .back:after {
  z-index: 2;
  transform-origin: 50% 0%;
  transform: perspective(160px) rotateX(180deg);
}

.M-Flipper.down .front:after,
.M-Flipper.down .back:before {
  z-index: 1;
}

.M-Flipper.down.go .front:before {
  transform-origin: 50% 100%;
  animation: frontFlipDown 0.6s ease-in-out both;
  box-shadow: 0 -2px 6px rgba(255, 255, 255, 0.3);
  backface-visibility: hidden;
}

.M-Flipper.down.go .back:after {
  animation: backFlipDown 0.6s ease-in-out both;
}

/*turn up*/
.M-Flipper.up .front:after {
  z-index: 3;
}

.M-Flipper.up .back:before {
  z-index: 2;
  transform-origin: 50% 100%;
  transform: perspective(160px) rotateX(-180deg);
}

.M-Flipper.up .front:before,
.M-Flipper.up .back:after {
  z-index: 1;
}

.M-Flipper.up.go .front:after {
  transform-origin: 50% 0;
  animation: frontFlipUp 0.6s ease-in-out both;
  box-shadow: 0 2px 6px rgba(255, 255, 255, 0.3);
  backface-visibility: hidden;
}

.M-Flipper.up.go .back:before {
  animation: backFlipUp 0.6s ease-in-out both;
}

@keyframes frontFlipDown {
  0% {
    transform: perspective(160px) rotateX(0deg);
  }

  100% {
    transform: perspective(160px) rotateX(-180deg);
  }
}

@keyframes backFlipDown {
  0% {
    transform: perspective(160px) rotateX(180deg);
  }

  100% {
    transform: perspective(160px) rotateX(0deg);
  }
}

@keyframes frontFlipUp {
  0% {
    transform: perspective(160px) rotateX(0deg);
  }

  100% {
    transform: perspective(160px) rotateX(180deg);
  }
}

@keyframes backFlipUp {
  0% {
    transform: perspective(160px) rotateX(-180deg);
  }

  100% {
    transform: perspective(160px) rotateX(0deg);
  }
}

.M-Flipper .number0:before,
.M-Flipper .number0:after {
  content: '0';
}

.M-Flipper .number1:before,
.M-Flipper .number1:after {
  content: '1';
}

.M-Flipper .number2:before,
.M-Flipper .number2:after {
  content: '2';
}

.M-Flipper .number3:before,
.M-Flipper .number3:after {
  content: '3';
}

.M-Flipper .number4:before,
.M-Flipper .number4:after {
  content: '4';
}

.M-Flipper .number5:before,
.M-Flipper .number5:after {
  content: '5';
}

.M-Flipper .number6:before,
.M-Flipper .number6:after {
  content: '6';
}

.M-Flipper .number7:before,
.M-Flipper .number7:after {
  content: '7';
}

.M-Flipper .number8:before,
.M-Flipper .number8:after {
  content: '8';
}

.M-Flipper .number9:before,
.M-Flipper .number9:after {
  content: '9';
}
</style>
