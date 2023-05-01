import { createApp } from 'vue'
import 'normalize.css'
import App from './App.vue'
// // 引入element plus
import ElementPlus from 'element-plus'
import 'element-plus/dist/index.css'
import "@/styles/reset.scss";
// import "@/assets/fonts/font.scss";
// CSS common style sheet
import "@/styles/common.scss";
import router from "./router";
import * as ElementPlusIconsVue from '@element-plus/icons-vue'
import vue3SeamlessScroll from "vue3-seamless-scroll";
import "@/assets/fonts/font.scss";

const app = createApp(App)
// 全局注册ElementPlus图标组件
for (const [key, component] of Object.entries(ElementPlusIconsVue)) {
    app.component(key, component)
}

app.use(vue3SeamlessScroll, {
    name: vue3SeamlessScroll.name
})

app.use(ElementPlus)
app.use(router)
app.mount('#app')
