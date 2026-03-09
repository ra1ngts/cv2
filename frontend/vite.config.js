import { defineConfig } from 'vite'
import { svelte } from '@sveltejs/vite-plugin-svelte'
import { resolve } from 'path'
import tailwindcss from '@tailwindcss/vite'

// https://vite.dev/config/
export default defineConfig({
  base: '/static/svelte/',  //'/static/svelte/assets/',
  plugins: [tailwindcss(), svelte()],
  resolve: {
    alias: {
      fonts: resolve('../static/svelte/fonts'),
      svg: resolve('../static/svelte/svg'),
    },
  },
  build: {
    // outDir: resolve('../main/static/svelte/assets'),
    outDir: resolve('../main/static/svelte'), // билдим в static/svelte
    assetsDir: 'assets',   // js/css будут в assets/
    chunkSizeWarningLimit: 1000,
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
