<template>
  <div class="dataScreen-container">
    <div class="dataScreen" ref="dataScreenRef">
      <div class="dataScreen-header">
        <div class="header-lf">
          <span class="header-screening">统计报告</span>
        </div>
        <div class="header-ct">
          <div class="header-ct-title">
            <span>中国的碳减排与世界能源消费展示平台</span>
            <div class="header-ct-warning">平台新闻信息（3条）</div>
          </div>
        </div>
        <div class="header-rg">
          <span class="header-download">统计报告</span>
          <span class="header-time">当前时间：{{ time }}</span>
        </div>
      </div>
      <div class="dataScreen-main">
        <div class="dataScreen-lf">
          <div class="dataScreen-top">
            <div class="dataScreen-main-title">
              <span>词云话题统计</span>
              <img src="@/images/dataScreen-title.png" alt="" />
            </div>
            <!-- chart区域 -->
            <div class="dataScreen-main-chart">
              <!-- <RealTimeAccessChart ref="RealTimeAccessRef" /> -->
              <WordCloud ref="WordCloudRef" />
            </div>
          </div>
          <div class="dataScreen-center">
            <div class="dataScreen-main-title">
              <span>全球碳排放量Top10</span>
              <img src="@/images/dataScreen-title.png" alt="" />
            </div>
            <!-- chart区域 -->
            <div class="dataScreen-main-chart">
              <MaleFemaleRatioChart ref="MaleFemaleRatioRef" />
            </div>
          </div>
          <div class="dataScreen-bottom">
            <div class="dataScreen-main-title">
              <span>中国发电装机容量占比</span>
              <img src="@/images/dataScreen-title.png" alt="" />
            </div>
            <!-- chart区域 -->
            <div class="dataScreen-main-chart">
              <AgeRatioChart ref="AgeRatioRef" />
            </div>
          </div>
        </div>
        <div class="dataScreen-ct">
          <div class="dataScreen-map">
            <div class="dataScreen-map-title">新闻概述</div>
            <div class="alarm-table">
              <!--          这里展示碳排放最多的省，包括碳排放总量和每个省份对应的质数排放总量的映射。  -->
              <vue3-seamless-scroll
                :list="alarmData"
                class="scroll-box"
                :step="0.5"
                :hover="true"
                :limitScrollNum="3"
              >
                <div class="map-list">
                  <div class="map-item" v-for="item in alarmData" :key="item.id">
                    <img src="@/images/dataScreen-alarm.png" alt="" />
                    <span class="map-alarm sle"
                      >{{ item.label }} 内容：{{ item.warnMsg }}</span
                    >
                  </div>
                </div>
              </vue3-seamless-scroll>
            </div>
            <div class="dataScreen-main-chart">
              <!-- <mapChart ref="MapChartRef" /> -->
              <CarbonChart ref="CarbonChartRef" @change="changeId" />
            </div>
          </div>
          <div class="dataScreen-cb">
            <div class="dataScreen-main-title">
              <span>中国不同年份产能占比</span>
              <img src="@/images/dataScreen-title.png" alt="" />
            </div>
            <!-- chart区域 -->
            <div class="dataScreen-main-chart">
              <OverNext30Chart ref="OverNext30Ref" />
            </div>
          </div>
        </div>
        <div class="dataScreen-rg">
          <div class="dataScreen-top">
            <div class="dataScreen-main-title">
              <span>2021年省份碳排量Top5</span>
              <img src="@/images/dataScreen-title.png" alt="" />
            </div>
            <!-- chart区域 -->
            <div class="dataScreen-main-chart">
              <HotPlateChart ref="HotPlateRef" />
            </div>
          </div>
          <div class="dataScreen-center">
            <div class="dataScreen-main-title">
              <span>中国年度碳排放对比</span>
              <img src="@/images/dataScreen-title.png" alt="" />
            </div>
            <!-- chart区域 -->
            <div class="dataScreen-main-chart">
              <AnnualUseChart ref="AnnualUseRef" />
            </div>
          </div>
          <div class="dataScreen-bottom">
            <div class="dataScreen-main-title">
              <span>中国能源消耗统计</span>
              <img src="@/images/dataScreen-title.png" alt="" />
            </div>
            <!-- chart区域 -->
            <div class="dataScreen-main-chart">
              <PlatformSourceChart ref="PlatformSourceRef" />
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts" name="Screen">
import { ref, Ref, onMounted, onBeforeUnmount } from 'vue'
// import { randomNum } from "@/utils";
// import { useRouter } from "vue-router";
import { useTime } from '../../utils/useTime'
import { ECharts } from 'echarts'
import WordCloud from './components/WordCloud.vue'
import CarbonChart from './components/CarbonChart.vue'
import AgeRatioChart from './components/AgeRatioChart.vue'
import AnnualUseChart from './components/AnnualUseChart.vue'
import HotPlateChart from './components/HotPlateChart.vue'
import MaleFemaleRatioChart from './components/MaleFemaleRatioChart.vue'
import OverNext30Chart from './components/OverNext30Chart.vue'
import PlatformSourceChart from './components/PlatformSourceChart.vue'
// import RealTimeAccessChart from './components/RealTimeAccessChart.vue';
import {getCarbonReqeust} from '../../axios/api/index'
// const router = useRouter();
const dataScreenRef = ref<HTMLElement | null>(null)
onMounted(() => {
  // 初始化时为外层盒子加上缩放属性，防止刷新界面时就已经缩放
  if (dataScreenRef.value) {
    dataScreenRef.value.style.transform = `scale(${getScale()}) translate(-50%, -50%)`
    dataScreenRef.value.style.width = `1920px`
    dataScreenRef.value.style.height = `1080px`
  }
  // 初始化 echarts
  initCharts()
  // 为浏览器绑定事件
  window.addEventListener('resize', resize)
})

// 根据浏览器大小推断缩放比例
const getScale = (width = 1920, height = 1080) => {
  let ww = window.innerWidth / width
  let wh = window.innerHeight / height
  return ww < wh ? ww : wh
}

// 监听浏览器 resize 事件
const resize = () => {
  if (dataScreenRef.value) {
    dataScreenRef.value.style.transform = `scale(${getScale()}) translate(-50%, -50%)`
  }
  // 使用了 scale 的echarts其实不需要需要重新计算缩放比例
  Object.values(dataScreen).forEach((chart) => {
    chart && chart.resize()
  })
}

// 声明echarts实例
interface ChartProps {
  [key: string]: ECharts | null
}
const dataScreen: ChartProps = {
  chart2: null,
  chart3: null,
  chart4: null,
  chart5: null,
  chart6: null,
  chart7: null,
  carbonChart: null,
  wordCloud: null,
}

// 获取子组件的ref
interface ChartExpose {
  initChart: (params: any) => ECharts
}

const AgeRatioRef = ref<ChartExpose>()
const AnnualUseRef = ref<ChartExpose>()
const HotPlateRef = ref<ChartExpose>()
const OverNext30Ref = ref<ChartExpose>()
const PlatformSourceRef = ref<ChartExpose>()
// const MapChartRef = ref<ChartExpose>();
const WordCloudRef = ref<ChartExpose>()

const provinceId = ref<number>(0)

const alarmData = ref([
  {
    id: 1,
    label: '中共中央 国务院关于完整准确全面贯彻新发展理念做好碳达峰碳中和工作的意见',
    warnMsg: '实现碳达峰、碳中和，是以习近平同志为核心的党中央统筹国内国际两个大局作出的重大战略决策，是着力解决资源环境约束突出问题、实现中华民族永续发展的必然选择，是构建人类命运共同体的庄严承诺。为完整、准确、全面贯彻新发展理念，做好碳达峰、碳中和工作，现提出如下意见',
  },
  {
    id: 2,
    label: '我国采取更加有力的政策和措施，持续推进绿色低碳发展 落实“双碳”行动 共建美丽家园',
    warnMsg: '今年“全国低碳日”主题为“落实‘双碳’行动，共建美丽家园”。党的十八大以来，我国以前所未有的力度推进生态文明建设，实施一系列应对气候变化战略、措施和行动，参与全球气候治理，绿色低碳发展取得了积极成效。',
  },
  {
    id: 3,
    label: '全国碳市场释放减排新动能',
    warnMsg: '全国碳排放权交易市场是我国利用市场机制控制和减少温室气体排放，推动绿色低碳发展的一项制度创新，也是落实我国碳达峰、碳中和的核心政策工具。截至12月22日，全国碳排放权交易市场累计成交额突破100亿元大关。全国碳市场正式上线以来，共运行350个交易日，碳排放配额累计成交量2.23亿吨，累计成交额101.21亿元。',
  },

])

// 初始化 charts参数
let ageData = [
  {
    value: 13.32,
    name: '火电',
    percentage: '52.0%',
  },
  {
    value: 3.926,
    name: '太阳能发电',
    percentage: '15.3%',
  },
  {
    value: 3.654,
    name: '风电',
    percentage: '14.3%',
  },
  {
    value: 4.135,
    name: '水电',
    percentage: '16.1%',
  },
  {
    value: 0.5182,
    name: '核电',
    percentage: '2.2%',
  },
  {
    value: 0.09128,
    name: '其他',
    percentage: '0.2%',
  },
]
let hotData = [
  {
    value: 93635.5,
    name: '山东省',
    percentage: '93.63%',
    maxValue: 100000,
  },
  {
    value: 83190.6,
    name: '内蒙古自治区',
    percentage: '83.19%',
    maxValue: 100000,
  },
  {
    value: 77836.8,
    name: '河北省',
    percentage: '77.84%',
    maxValue: 100000,
  },
  {
    value: 73356.1,
    name: '江苏省',
    percentage: '73.35%',
    maxValue: 100000,
  },
  {
    value: 55806.6,
    name: '广东省',
    percentage: '55.08%',
    maxValue: 100000,
  },
]
let annualData = [
  {
    label: new Date().getFullYear() - 2 + '年',
    value: ['184', '90', '120', '0', '30', '100', '80', '40', '20', '510', '350', '180'],
  },
  {
    label: new Date().getFullYear() - 1 + '年',
    value: [
      '118',
      '509',
      '366',
      '162',
      '380',
      '123',
      '321',
      '158',
      '352',
      '474',
      '154',
      '22',
    ],
  },
  {
    label: new Date().getFullYear() + '年',
    value: [
      '548',
      '259',
      '113',
      '90',
      '69',
      '512',
      '23',
      '49',
      '28',
      '420',
      '313',
      '156',
    ],
  },
]
const getCarbonList = async () => {
  const yearList = (await getCarbonReqeust()).data
  annualData = yearList
  console.log(annualData)
  return annualData.splice(0,1)
}

(async () => {
  const result = await getCarbonList()
  console.log(result)
})()


// 初始化 echarts
const initCharts = async (): Promise<void> => {
  await getCarbonList(); // 等待 annualData 被赋值
  dataScreen.chart2 = AgeRatioRef.value?.initChart(ageData) as ECharts
  dataScreen.chart3 = AnnualUseRef.value?.initChart({
    data: annualData,
    unit: annualData.map((val) => val.label),
    columns: ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12'],
    colors: ['#FFA600', '#007AFE', '#FF4B7A'],
  }) as ECharts
  dataScreen.chart4 = HotPlateRef.value?.initChart({
    data: hotData,
    colors: ['#1089E7', '#F57474', '#56D0E3', '#F8B448', '#8B78F6'],
  }) as ECharts
  dataScreen.chart6 = OverNext30Ref.value?.initChart({
    data: new Array(30).fill('').map((val) => {
      val = 10000
      return val
    }),
  }) as ECharts
  // dataScreen.mapChart = MapChartRef.value?.initChart(mapData) as ECharts;
}

const changeId = (e: any): void => {
  provinceId.value = e
  console.log('父组件接收子组件传过来的provinceId', provinceId.value)
}

// 获取当前时间
const { nowTime } = useTime()
let timer: NodeJS.Timer | null = null
let time: Ref<string> = ref(nowTime.value)
timer = setInterval(() => {
  time.value = useTime().nowTime.value
}, 1000)

// 销毁时触发
onBeforeUnmount(() => {
  window.removeEventListener('resize', resize)
  clearInterval(timer!)
  Object.values(dataScreen).forEach((val) => val?.dispose())
})
</script>
<style lang="scss" scoped>
@import '../../index.scss';
</style>
