<template>
  <!-- 全球碳排量 -->
  <div class="actual-box">
    <div class="echarts-header">
      <span>排名</span>
      <span>国家</span>
      <span>排放量(吨)</span>
    </div>
    <div class="actutal-table">
      <vue3-seamless-scroll
        :list="rankData"
        class="scroll-box"
        :step="0.5"
        :hover="true"
        :limitScrollNum="5"
      >
        <div class="actutal-list">
         
          <div class="actutal-item" v-for="item in rankData" :key="item.id">
            
            <span class="item-txt item-pm"><b>{{ item.pm }}</b></span>
           
            <span class="item-txt">{{ item.sf }}</span>
           
            <span class="item-txt">{{ item.pfl }}</span>
          </div>
        </div>
      </vue3-seamless-scroll>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, watchEffect } from 'vue';
import {getWorldReqeust} from '../../../axios/api/index'
const rankData = ref([])

async function rankResult() {
  const result = await getWorldReqeust()
  rankData.value = result.data
}
rankResult()
watchEffect(() => {
  console.log(rankData.value) // 确认数据成功获取并更新
})

</script>
<style lang="scss" scoped>
.echarts {
  width: 100%;
  height: calc(100% - 50px);
}
.actual-box {
  .echarts-header {
    box-sizing: border-box;
    display: flex;
    height: 36px;
    margin: 10px 10px 0;
    line-height: 36px;
    background: url('@/images/rankingChart-bg.png') no-repeat;
    background-size: 100% 100%;
    span {
      width: 18%;
      margin-left: 4px;
      font-size: 14px;
      font-weight: bold;
      color: #fdbc52;
      text-align: center;
      &:nth-child(2) {
        margin-left: 4px;
      }
      &:last-child {
        width: 30%;
        margin-left: 40px;
      }
    }
  }
  .actutal-table {
    .scroll-box {
      height: 180px;
      overflow: hidden;
    }
    .actutal-list {
      .actutal-item {
        box-sizing: border-box;
        display: flex;
        height: 30px;
        margin: 10px 10px 0;
        line-height: 30px;
        text-align: center;
        color: #fff;
        &:nth-child(2n) {
          background-color: rgba(255,255,255,.1);
        }
        &:nth-child(8n-4) {
          .item-pm {
            b {
              background: #20a8fe;
            }
          }
        }
        &:nth-child(8n-3) {
          .item-pm {
            b {
              background: #EB6841;
            }
          }
        }
        &:nth-child(8n-2) {
          .item-pm {
            b {
              background: #3FB8AF;
            }
          }
        }
        &:nth-child(8n-1) {
          .item-pm {
            b {
              background: #FE4365;
            }
          }
        }
        &:nth-child(8n-5) {
          .item-pm {
            b {
              background: #FC9D9A;
            }
          }
        }
        &:nth-child(8n-6) {
          .item-pm {
            b {
              background: #EDC951;
            }
          }
        }
        &:nth-child(8n-7) {
          .item-pm {
            b {
              background: #C8C8A9;
            }
          }
        }
        &:nth-child(8n) {
          .item-pm {
            b {
              background: #83AF9B;
            }
          }
        }
        &:first-child {
          .item-pm {
            b {
              background: #036564;
            }
          }
        }
        &:last-child {
          .item-pm {
            b {
              background: #3299BB;
            }
          }
        }
        .item-txt {
          &.item-pm {
            b {
              display: inline-block;
              width: 20px;
              height: 20px;
              border-radius: 3px;
              color: #ffffff;
              line-height: 20px;
            }
          }
          width: 18%;
          &:nth-child(2) {
            margin-left: 4px;
          }
          &:last-child {
            width: 20%;
            margin-left: 60px;
          }
        }
      }
    }
  }
}
</style>
