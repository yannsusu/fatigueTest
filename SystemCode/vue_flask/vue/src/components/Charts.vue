<!-- eslint-disable vue/multi-word-component-names -->
<template>
    <div class="charts">
        <e-charts class="BlinkYawn" :option="blinkyawnoption" />
        <e-charts class="Lean" :option="leanoption"/>
    </div>
</template>

<script setup>
    import { ref, computed } from 'vue';
    import axios from 'axios';
    
    
    const BlinkYawnData = ref([
        { blinkvalue: 0,  yawnvalue: 0, name: '1' },
        { blinkvalue: 0,  yawnvalue: 0, name: '2' },
        { blinkvalue: 0,  yawnvalue: 0, name: '3' },
        { blinkvalue: 0,  yawnvalue: 0, name: '4' },
        { blinkvalue: 0,  yawnvalue: 0, name: '5' },
        { blinkvalue: 0,  yawnvalue: 0, name: '6' },
        { blinkvalue: 0,  yawnvalue: 0, name: '7' },
        { blinkvalue: 0,  yawnvalue: 0, name: '8' },
        { blinkvalue: 0,  yawnvalue: 0, name: '9' },
        { blinkvalue: 0,  yawnvalue: 0, name: '10' },
    ]);
    const LeanData = ref([
    { leanvalue: 0, name: '1' },
        { leanvalue: 0, name: '2' },
        { leanvalue: 0, name: '3' },
        { leanvalue: 0, name: '4' },
        { leanvalue: 0, name: '5' },
        { leanvalue: 0, name: '6' },
        { leanvalue: 0, name: '7' },
        { leanvalue: 0, name: '8' },
        { leanvalue: 0, name: '9' },
        { leanvalue: 0, name: '10' },
    ]);

    const fetchData_nap = () => {
        axios.get('http://127.0.0.1:5000/nap', {
            headers: {
                'Access-Control-Allow-Origin': '*'
            }
        })
        .then(response => {
            console.log(response.data);
            BlinkYawnData.value = response.data.map((item ,index) => ({
                blinkvalue: item[0],
                yawnvalue: item[1],
                name: (index + 1).toString()
            }));
        console.log('success')
        
        })
        .catch(error => {
            console.error(error);
            console.log('error')
        });

    }

    const fetchData_lean = () => {
        axios.get('http://127.0.0.1:5000/lean', {
            headers: {
                'Access-Control-Allow-Origin': '*'
            }
        })
        .then(response => {
            console.log(response.data);
            LeanData.value = response.data.map((item ,index) => ({
                leanvalue: item[0],
                name: (index + 1).toString()
            }));
        console.log('success')
        })
        .catch(error => {
            console.error(error);
            console.log('error')
        });
    }

    fetchData_nap();
    fetchData_lean();
    fetchData_video();
    // Refresh data at regular intervals
    setInterval(fetchData_nap, 1000);
    setInterval(fetchData_lean, 1000);
    setInterval(fetchData_video, 500);


    const blinkyawnoption = computed(() => {
        return {
            color: [
                '#d87c7c','#d7ab82',
            ],
            title: {
                text: 'User blink count',
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
                data: BlinkYawnData.value.map(d => d.name),
                "axisLabel":{interval: 0}
            },
            yAxis: {
                type: 'value',
            },

            visualMap: [
                {
                    type: 'piecewise',
                    show: false,
                    orient: 'horizontal',
                    dimension: 1,
                    seriesIndex: 0,
                    pieces: [
                    {
                        gt: 0.5,
                        lt: 1,
                        color: 'rgba(0, 0, 180, 0.4)'
                    },
                    ]
                     
                },

            ],
            
            series: [
                {
                    name:"bink times",
                    data: BlinkYawnData.value.map(d => d.blinkvalue),
                    type: 'line',
                    smooth: 0.3,
                    lineStyle: {
                        color: '#5470C6',
                        width: 2
                    },
                    symbolSize: 5,
                    symbol: 'circle',

                    areaStyle: {},
                },

                {
                    name:"yawn times",
                    data: BlinkYawnData.value.map(d => d.yawnvalue),
                    type: 'line',
                    smooth: 0.3,
                    lineStyle: {
                        color: '#d87c7c',
                        width: 2
                    },
                    symbolSize: 5,
                    symbol: 'circle',
                },
            ],
        }
    });
  
    const leanoption = computed(() => {
        return {
            title: {
                text: 'User body tilt data',
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
                data: LeanData.value.map(d => d.name),
                "axisLabel":{interval: 0}
            },
            yAxis: {
                type: 'value',
            },

            visualMap: {
                type: 'piecewise',
                show: false,
                orient: 'horizontal',
                dimension: 1,
                seriesIndex: 0,
                pieces: [
                {
                    gt: 80,
                    lt: 100,
                    color: 'rgba(0, 0, 180, 0.4)'
                },
                ]
            },
            
            series: [
            {
                name:"Angle",
                data: LeanData.value.map(d => d.leanvalue),
                type: 'line',
                smooth: 0.3,
                lineStyle: {
                    color: '#5470C6',
                    width: 2
                },
                symbolSize: 5,
                symbol: 'circle',

                areaStyle: {},

            
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
  .BlinkYawn{
    width: 50%;
    height: 400px;
    border-radius: 30px;
    margin-top: 5%;
    margin-left: 3%;
    display: inline-block;
    align-content: center;
  }
  .Lean{
    width: 50%;
    height: 400px;
    margin-top: 5%;
    margin-right: 3%;
    display: inline-block; 
    border-radius: 30px;
    align-content: center;
  }
  </style>