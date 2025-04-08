<!-- eslint-disable vue/multi-word-component-names -->
<template>
    <div class="charts">
        <e-charts class="blink" :option="blinkoption" />
        <e-charts class="canteen" :option="canteenoption"/>
    </div>
</template>

<script setup>
    import { ref, computed } from 'vue';
    const BlinkData = ref([
        { value: 0,  name: '1' },
        { value: 0,  name: '2' },
        { value: 0,  name: '3' },
        { value: 0,  name: '4' },
        { value: 0,  name: '5' },
        { value: 0,  name: '6' },
        { value: 0,  name: '7' },
        { value: 0,  name: '8' },
        { value: 0,  name: '9' },
        { value: 0,  name: '10' },
    ]);
    const LibraryData = ref([
        { value1: 0, value2: 0, name: '图书馆主馆' },
        { value1: 0, value2: 0, name: '李政道图书馆' },
        { value1: 0, value2: 0, name: '包玉刚图书馆' },
        { value1: 0, value2: 0, name: '徐汇社科馆' },
    ]);
    setInterval(() => {
        BlinkData.value = BlinkData.value.map(item => ({
        ...item,
        value: Math.random() * 100,
        }));
    }, 5000);
    
    setInterval(() => {
        LibraryData.value = LibraryData.value.map(item => ({
        ...item,
        value1: Math.random() * 100,
        }));
    }, 5000);
    setInterval(() => {
        LibraryData.value = LibraryData.value.map(item => ({
        ...item,
        value2: Math.random() * 100,
        }));
    }, 5000);

    const blinkoption = computed(() => {
        return {
            color: [
                '#d87c7c','#d7ab82',
            ],
            title: {
                text: 'User blink & yawn count',
                x:'center',
                y:'top'
            },
            tooltip: {
                trigger: 'axis',
                axisPointer: {
                type: 'shadow'
                }   
            },
            toolbox: {
                show: true,
                orient: 'vertical',
                left: 'right',
                top: 'center',
                feature: {
                mark: { show: true },
                dataView: { show: true, readOnly: false },
                magicType: { show: true, type: ['bar', 'line'] },
                restore: { show: true },
                saveAsImage: { show: true }
                }
            },
            legend: {
                orient: 'horizontal',
                x:'right',
                y:'top',
            },
            xAxis: {
                type: 'category',
                data: BlinkData.value.map(d => d.name),
                "axisLabel":{interval: 0}
            },
            yAxis: {
                type: 'value',
            },
            series: [
            {
                name:"frequency",
                data: BlinkData.value.map(d => d.value),
                type: 'bar',
            },
            ],
        }
    });
  
    const canteenoption = computed(() => {
        return {
            title: {
                text: 'Degree of body sway',
                x:'center',
                y:'top',
            },
            tooltip: {
                trigger: 'axis',
                axisPointer: {
                type: 'shadow'
                }   
            },
            toolbox: {
                show: true,
                orient: 'vertical',
                left: 'right',
                top: 'center',
                feature: {
                mark: { show: true },
                dataView: { show: true, readOnly: false },
                magicType: { show: true, type: ['bar', 'stack'] },
                restore: { show: true },
                saveAsImage: { show: true }
                }
            },
            legend: {
                orient: 'horizontal',
                x:'right',
                y:'top',
            },
            xAxis: {
                type: 'category',
                data: BlinkData.value.map(d => d.name),
                "axisLabel":{interval: 0}
            },
            yAxis: {
                type: 'value',
            },
            series: [
            {
                name:"frequency",
                data: BlinkData.value.map(d => d.value),
                type: 'line',
                smooth: 0.3,
                lineStyle: {
                    color: '#5470C6',
                    width: 2
                },
                symbolSize: 5,
                symbol: 'circle',
            },

            ],
        }
    });
</script>

<style scoped>
  .charts {
    width: 80%;
    margin-left:10%;
    margin-top: 9%;
    height: 450px;
    margin-bottom: 7%;
    background-color: rgba(255, 255, 255, 0.759);
    border-radius: 30px;
    display: flex;
    align-content: center;
  }
  .blink{
    width: 50%;
    height: 400px;
    border-radius: 30px;
    margin-top: 5%;
    margin-left: 3%;
    display: inline-block;
    align-content: center;
  }
  .canteen{
    width: 50%;
    height: 400px;
    margin-top: 5%;
    margin-right: 3%;
    display: inline-block; 
    border-radius: 30px;
    align-content: center;
  }
  </style>