import Vue from 'https://cdn.jsdelivr.net/npm/vue@latest/dist/vue.esm.browser.js'

export default(Vue.component('navbar-item', {
    props: ['route'],
    template: `
    <li :class="'nav-item ' + route.active">
        <a class="nav-link" :href="route.route">{{route.title}}<span class="sr-only" v-if="route.active === 'active'"> (current)</span></a>
    </li>`
}))