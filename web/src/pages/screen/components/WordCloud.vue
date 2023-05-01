<template>
  <!-- 词云图 -->
  <div class="echarts-box">
    <div class="echarts" id="wordCloud"></div>
  </div>
</template>

<script setup lang="ts">
import { ECharts, EChartsOption, init } from 'echarts'
import 'echarts-wordcloud'
import { onMounted, ref,watchEffect} from 'vue'
import { GetListTestRequest } from '../../../axios/api/index'

const newData = ref([])

const wordCloud = async () => {
  const dataList = (await GetListTestRequest()).data
  newData.value = dataList
  // console.log(dataList)
}

//@ts-ignore
const initChart = (): ECharts => {
  const charEle = document.getElementById('wordCloud') as HTMLElement
  const charEch: ECharts = init(charEle)
  const option: EChartsOption = {
    tooltip: {
      show: false,
    },
    series: [
      {
        type: 'wordCloud',
        gridSize: 5,
        shape: 'circle',
        sizeRange: [12, 32],
        width: '100%',
        height: '100%',
        rotationRange: [-45, 0, 45, 90],
        drawOutOfBound: false,
        //当单词较多时禁用会导致UI阻塞。
        layoutAnimation: true,
        textStyle: {
          fontFamily: 'sans-serif',
          fontWeight: 'bold',
          // 任意颜色
          color: function () {
            return (
              'rgb(' +
              [
                Math.round(Math.random() * 500),
                Math.round(Math.random() * 300),
                Math.round(Math.random() * 200),
              ].join(',') +
              ')'
            )
          },
        },
        emphasis: {
          focus: 'self',
          textStyle: {
            textShadowBlur: 10,
            textShadowColor: '#333',
          },
        },
        left: 'center',
        top: 'center',
        right: '',
        bottom: '',
        data: newData.value,
      },
    ],
  }
  charEch.setOption(option)
  return charEch
}

onMounted(async () => {
  await wordCloud()
  const charEch = initChart()
  watchEffect(() => {
    charEch.setOption({
      series: [
        {
          data: newData.value,
        },
      ],
    })
  })
})

defineExpose({
  initChart,
})
</script>

<style lang="scss" scoped>
.echarts-box {
  width: 100%;
  height: 100%;
  #wordCloud {
    height: 300px;
  }
}
</style>
