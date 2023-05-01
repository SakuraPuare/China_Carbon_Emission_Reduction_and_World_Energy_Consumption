<template>
  <!-- 未来30天访问量趋势预测图 -->
  <div class="echarts" id="OverNext30Chart"></div>
</template>

<script setup lang="ts">
import { ECharts, EChartsOption, init } from 'echarts'

//@ts-ignore
const initChart = (data: any = {}): ECharts => {
  const charEle = document.getElementById('OverNext30Chart') as HTMLElement
  const charEch: ECharts = init(charEle)
  const option: EChartsOption = {
    color: ['#fd8f1e', '#7cb5ec', '#4280f1', '#957bde'],
    tooltip: {
      trigger: 'axis',
      axisPointer: {
        // 坐标轴指示器，坐标轴触发有效
        type: 'shadow', // 默认为直线，可选为：'line' | 'shadow'
      },
    },
    grid: {
      left: '15%',
      right: '6%',
      bottom: '10%',
      top: '3%',
      containLabel: true,
      z: 22,
    },
    legend: {
      orient: 'vertical',
      data: ['原煤(亿吨)', '原油(亿吨)', '天然气(千亿立方米)', '电力(万亿千瓦时)'],
      textStyle: {
        fontSize: 12,
        color: '#fff',
      },
      icon: 'rect',
      itemWidth: 10,
      itemHeight: 10,
      itemGap: 20,
      top: '15%',
      left: 0,
    },
    xAxis: [
      {
        name: '产量',
        nameTextStyle: {
          color: '#fff',
        },
        axisLabel: {
          color: '#fff',
          fontSize: 12,
        },
        splitLine: {
          lineStyle: {
            color: '#24214e',
          },
        },
        axisLine: {
          lineStyle: {
            type: 'solid',
            color: '#24214e',
            width: 1, // 坐标线的宽度
          },
        },
      },
    ],
    yAxis: [
      {
        data: ['2022', '2021', '2020', '2019'],
        axisLabel: {
          color: '#fff',
          fontSize: 12, //坐标值得具体的颜色
        },
        axisLine: {
          lineStyle: {
            type: 'solid',
            color: '#24214e',
            width: 1, //坐标线的宽度
          },
        },
      },
    ],
    series: [
      {
        name: '原煤(亿吨)',
        type: 'bar',
        stack: '总量',
        barWidth: 20,
        label: {
          show: false,
          position: 'insideRight',
        },
        data: [45.0, 41.3, 39.02, 38.46],
      },
      {
        name: '原油(亿吨)',
        type: 'bar',
        barWidth: 20,
        stack: '总量',
        label: {
          show: false,
          position: 'insideRight',
        },
        data: [2.0467, 1.98881, 1.94768, 1.916283],
      },
      {
        name: '天然气(千亿立方米)',
        type: 'bar',
        stack: '总量',
        barWidth: 20,
        label: {
          show: false,
          position: 'insideRight',
        },
        data: [2.178, 2.0758, 1.92494,1.75362],
      },
      {
        name: '电力(万亿千瓦时)',
        type: 'bar',
        stack: '总量',
        barWidth: 20,
        label: {
          show: false,
          position: 'insideRight',
        },
        data: [8.4,8.53425, 7.77906, 7.503428],
      },
    ],
  }
  charEch.setOption(option)
  return charEch
}

defineExpose({
  initChart,
})
</script>

<style lang="scss" scoped>
.echarts {
  width: 100%;
  height: 100%;
  :deep(.lineChart-bg) {
    box-sizing: border-box;
    display: flex;
    align-items: center;
    width: 180px;
    height: 60px;
    padding-left: 20px;
    background: url('@/images/line-bg.png') no-repeat;
    background-size: 100% 100%;
    span {
      font-size: 12px;
      color: rgb(255 255 255 / 80%);
      i {
        font-style: normal;
        color: #f5b348;
      }
    }
  }
}
</style>
