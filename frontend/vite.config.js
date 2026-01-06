import { defineConfig } from 'vite'
import { svelte } from '@sveltejs/vite-plugin-svelte'
import { resolve } from 'path'

// https://vite.dev/config/
export default defineConfig({
  base: '/static/svelte/assets/',
  plugins: [svelte()],
  resolve: {
    alias: {
      fonts: resolve('../static/svelte/fonts'),
      svg: resolve('../static/svelte/svg'),
    },
  },
  build: {
    outDir: resolve('../main/static/svelte/assets'),
    chunkSizeWarningLimit: 1000,
    assetsDir: '',
    manifest: true,
    emptyOutDir: true,
    watch: {},
  },
  server: {
    watch: {
      usePolling: true,
      interval: 100,
    },
    port: 8000,
    hot: true,
  },
});
