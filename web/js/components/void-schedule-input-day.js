import Vue from 'https://cdn.jsdelivr.net/npm/vue@latest/dist/vue.esm.browser.js'
import assets from '../assets.js';
import voidscheduleinputrow from "./void-schedule-input-row.js"

export default(Vue.component('void-schedule-input-day', {
    data: () => {
        return {
            assets: assets
        }
    },
    components: {
        "void-schedule-input-row": voidscheduleinputrow
    },
    /*template*/
    template: `
    <div class="container">
        <void-schedule-input-row 
            v-bind:rowdata="asset.data" 
            v-for="asset in assets" 
            v-bind:key="asset.key">
        </void-schedule-input-row>
    </div>
    `
}))