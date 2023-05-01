<template>
  <div class="no-fond">
    <img
      src="./404.jpeg"
      @click="$router.replace('/')"
      alt="图片加载失败！"
      title="请返回首页，重新查找url！"
    />
  </div>
</template>
<style lang="scss" scoped>
.no-fond {
  position: relative;
  width: 100%;
  height: 99.8vh;
  overflow: hidden;
  background-color: #fafafa;
}
img {
  position: absolute;
  left: 50%;
  top: 60%;
  transform: translate(-50%, -50%);
  font-size: 0;
  margin: 0;
  padding: 0;
  position: relative;
}
</style>
