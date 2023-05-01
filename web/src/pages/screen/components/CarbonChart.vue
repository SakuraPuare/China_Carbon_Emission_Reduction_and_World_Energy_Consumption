<template>
  <!-- 中国碳排放 -->
  <div class="echarts-box">
    <div class="echarts" id="carbonChart"></div>
  </div>
</template>

<script setup lang="ts">
import { ECharts, EChartsOption, init } from 'echarts';
import { onMounted } from 'vue';

const emit = defineEmits(['change'])
//@ts-ignore
const initChart = (): ECharts => {
  const charEle = document.getElementById('carbonChart') as HTMLElement;
  const charEch: ECharts = init(charEle);
  const option: EChartsOption = {
    tooltip: {
      trigger: 'item'
    },
    legend: {
      top: 'bottom',
      textStyle: {
        color: '#ffffff',
      },
    },
    toolbox: {
      show: true,
      top: '15%',
      right: '2%',
      iconStyle: {
        borderColor: '#05e8fe', // 图标默认颜色
      },
      feature: {
        mark: { show: true },
        dataView: { show: true, readOnly: false },
        restore: { show: true },
        saveAsImage: { show: true },
      },
    },
    series: [
      {
        name: '2021年中国各省碳排量总量(万吨)',
        type: 'pie',
        radius: [50, 200],
        center: ['50%', '50%'],
        roseType: 'area',
        itemStyle: {
          borderRadius: 8,
        },
        label: {
          color: '#fff',
        },
        data: [
          { id: 1, value: 8878.9, name: '北京市' },
          { id: 2, value: 25285.6, name: '天津市' },
          { id: 4, value: 77836.8, name: '河北省' },
          { id: 5, value: 54408.5, name: '山西省' },
          { id: 6, value: 83190.6, name: '内蒙古自治区' },
          { id: 7, value: 48766.3, name: '辽宁省' },
          { id: 8, value: 20063.2, name: '吉林省' },
          { id: 9, value: 26475.7, name: '黑龙江省' },
          { id: 10, value: 16744.2, name: '上海市' },
          { id: 11, value: 73356.1, name: '江苏省' },
          { id: 12, value: 38797.5, name: '浙江省' },
          { id: 13, value: 40711.1, name: '安徽省' },
          { id: 14, value: 27887.4, name: '福建省' },
          { id: 15, value: 22542.3, name: '江西省' },
          { id: 16, value: 93635.5, name: '山东省' },
          { id: 17, value: 47515.7, name: '河南省' },
          { id: 18, value: 29439.4, name: '湖北省' },
          { id: 19, value: 27168.8, name: '湖南省' },
          { id: 20, value: 55806.6, name: '广东省' },
          { id: 21, value: 24573.8, name: '广西壮族自治区' },
          { id: 22, value: 4212.9, name: '海南省' },
          { id: 23, value: 14580.1, name: '重庆市' },
          { id: 24, value: 28231.9, name: '四川省' },
          { id: 25, value: 23549.4, name: '贵州省' },
          { id: 26, value: 21073.0, name: '云南省' },
          { id: 27, value: 764.6, name: '西藏自治区' },
          { id: 28, value: 29451.3, name: '陕西省' },
          { id: 29, value: 17382.9, name: '甘肃省' },
          { id: 30, value: 4556, name: '青海省' },
          { id: 31, value: 22186.3, name: '宁夏回族自治区' },
          { id: 32, value: 47894.4, name: '新疆维吾尔自治区' },
        ],
      },
    ],
  };
  charEch.setOption(option);
  charEch.on("click",function(params: any){
    emit('change', params.data.id)
    console.log('params.data.id', params.data.id);
  })
};

onMounted(() => {
  initChart();
});

defineExpose({
  initChart,
});
</script>

<style lang="scss" scoped>
.echarts-box {
  position: relative;
  width: 100%;
  height: 100%;
  z-index: 101;
  #carbonChart {
    width: 970px;
    height: 670px;
    margin: 0 auto;
  }
}
</style>
