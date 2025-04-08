<template>
  <div class="FlipClock">
    <Flipper ref="flipperHour1" />
    <Flipper ref="flipperHour2" />
    <em>:</em>
    <Flipper ref="flipperMinute1" />
    <Flipper ref="flipperMinute2" />
    <em>:</em>
    <Flipper ref="flipperSecond1" />
    <Flipper ref="flipperSecond2" />
  </div>
</template>

<script>
import Flipper from './Flipper.vue'

export default {
  name: 'FlipClock',
  data () {
    return {
      timer: null,
      flipObjs: []
    }
  },
  components: {
    Flipper
  },
  methods: {
    // Initialize numbers
    init () {
      let now = new Date()
      let nowTimeStr = this.formatDate(new Date(now.getTime()), 'hhiiss')
      for (let i = 0; i < this.flipObjs.length; i++) {
        this.flipObjs[i].setFront(nowTimeStr[i])
      }
    },
    // start counting
    run () {
      this.timer = setInterval(() => {
        // Get current time
        let now = new Date()
        let nowTimeStr = this.formatDate(new Date(now.getTime() - 1000), 'hhiiss')
        let nextTimeStr = this.formatDate(now, 'hhiiss')
        for (let i = 0; i < this.flipObjs.length; i++) {
          if (nowTimeStr[i] === nextTimeStr[i]) {
            continue
          }
          this.flipObjs[i].flipDown(
            nowTimeStr[i],
            nextTimeStr[i]
          )
        }
      }, 1000)
    },
    // Regularly Formatted Dates
    formatDate (date, dateFormat) {
      /* Format the year individually and output the year based on the number of characters in y
     * example：yyyy => 2019
            yy => 19
            y => 9
     */
      if (/(y+)/.test(dateFormat)) {
        dateFormat = dateFormat.replace(
          RegExp.$1,
          (date.getFullYear() + '').substr(4 - RegExp.$1.length)
        )
      }
      // Format month, day, hour, minute, second
      let o = {
        'm+': date.getMonth() + 1,
        'd+': date.getDate(),
        'h+': date.getHours(),
        'i+': date.getMinutes(),
        's+': date.getSeconds()
      }
      for (let k in o) {
        if (new RegExp(`(${k})`).test(dateFormat)) {
          // Retrieve the corresponding value
          let str = o[k] + ''
          /* Outputs the corresponding characters according to the set format
           * Example: 8am, hh => 08, h => 8
           * However, when the number >= 10, no intercept is done, regardless of whether the format is one or more digits, which is inconsistent with year formatting
           * Example: 15 p.m., hh => 15, h => 15
           */
          dateFormat = dateFormat.replace(
            RegExp.$1,
            RegExp.$1.length === 1 ? str : this.padLeftZero(str)
          )
        }
      }
      return dateFormat
    },
    // date and time zero replenishment
    padLeftZero (str) {
      return ('00' + str).substr(str.length)
    }
  },
  mounted () {
    this.flipObjs = [
      this.$refs.flipperHour1,
      this.$refs.flipperHour2,
      this.$refs.flipperMinute1,
      this.$refs.flipperMinute2,
      this.$refs.flipperSecond1,
      this.$refs.flipperSecond2
    ]
    this.init()
    this.run()
  }
}
</script>

<style scoped>
.FlipClock {
    text-align: center;
}
.FlipClock .M-Flipper {
    margin: 0 3px;
}
.FlipClock em {
    display: inline-block;
    line-height: 76px;
    font-size: 56px;
    font-style: normal;
    vertical-align: top;
}
</style>
