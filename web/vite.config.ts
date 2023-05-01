import {defineConfig} from 'vite'
import vue from '@vitejs/plugin-vue'
import {resolve} from "path";
// https://vitejs.dev/config/
export default defineConfig({
    plugins: [vue()],
    server: {
        port: 8888,
        proxy: {
            '/api': {
                target: 'https://carbon.sakurapuare.com/api',
                changeOrigin: true,
                rewrite: (path) => path.replace(/^\/api/, '') // 不可以省略rewrite  axois.post('/api/xxx', data)
            }
        }
    },
    resolve: {
        alias: [
            {
                find: '@', // 配置别名，tsconfig.json里面也需要配置. @等价于src
                replacement: resolve(__dirname, 'src')
            }
        ]
    },
  build: {
        rollupOptions: {
            output: {
                manualChunks(id) {
                    if (id.includes('node_modules')) {
                        return id
                            .toString()
                            .split('node_modules/')[1]
                            .split('/')[0]
                            .toString()
                    }
                },
            },
        },
    },
    css: {
        preprocessorOptions: {
            scss: {
                additionalData: `@import "@/styles/var.scss";`
            }
        }
    },
})
