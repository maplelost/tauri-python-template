import { createApp } from "vue";
import App from "./App.vue";

createApp(App).mount("#app");

// tauri
import { getCurrentWindow } from "@tauri-apps/api/window";
import pythonApi from "./python_api";

const isProd = import.meta.env.PROD;
const onCloseRequested = await getCurrentWindow().onCloseRequested(
  async (event) => {
    if (isProd) {
      await pythonApi.shutdown();
    }
    await getCurrentWindow().destroy();
  }
);
