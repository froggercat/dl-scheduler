import Vue from 'https://cdn.jsdelivr.net/npm/vue@latest/dist/vue.esm.browser.js'
import navbaritem from './navbar-item.js'

export default(Vue.component('navbar', {
    props: ['routes'],
    components: {
        "navbar-item": navbaritem
    },
    /*template*/
    template: `
    <nav class="navbar navbar-expand-lg">
        <a class="navbar-brand" href="#">Navbar</a>
            <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
            <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarSupportedContent">
            <ul class="navbar-nav mr-auto">
                <navbar-item
                    v-for="route in routes"
                    v-bind:route="route"
                    v-bind:key="route.id">
                </navbar-item>
            </ul>
        </div>
    </nav>`
}));
