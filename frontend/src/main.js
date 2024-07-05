import 'vue-toast-notification/dist/theme-bootstrap.css';

import App from './App.vue'
import ToastPlugin from 'vue-toast-notification';
import { createApp } from 'vue'
import { loadFonts } from './plugins/webfontloader'
import router from './router'
import store from './store'
import vuetify from './plugins/vuetify'

loadFonts()

// const options = {
//   // You can set your default options here
//   position: "top-right",
//   timeout: 5000,
//   closeOnClick: true,
//   pauseOnFocusLoss: true,
//   pauseOnHover: true,
//   draggable: true,
//   draggablePercent: 0.6,
//   showCloseButtonOnHover: false,
//   hideProgressBar: true,
//   closeButton: "button",
//   icon: true,
//   rtl: false
// };

createApp(App).use(store)
  .use(ToastPlugin)
  .use(router)
  .use(vuetify)
  .mount('#app')
