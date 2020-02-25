import Vue from 'https://cdn.jsdelivr.net/npm/vue@latest/dist/vue.esm.browser.js'

export default(Vue.component('void-schedule-input-row', {
    props: ['rowdata'],
    data() {
        let elements = ["fire", "water", "wind", "light", "shadow"];
        let default_images = elements.map(element => {
            let img_exists = this.$props.rowdata.filter((v, i)=>{
                return v.hasOwnProperty("element") && v.element === element;
            });
            if (img_exists.length > 0) {
                let single_drops_exists = img_exists[0].images.hasOwnProperty("path");
                return {[element]: {
                    path: single_drops_exists ?
                        img_exists[0].images.path :
                        img_exists[0].images["2x"] }}
            }
            let non2xdrops = this.$props.rowdata.filter((v)=> { return v.images.hasOwnProperty("path")});
            return {[element]: {path: non2xdrops.length > 0 ? 
                non2xdrops[0].images.path : 
                this.$props.rowdata[0].images["2x"]}};
        });
        let double_drops_images = elements.map(element => {
            let img_exists = this.$props.rowdata.filter((v, i)=>{
                return v.hasOwnProperty("element") && v.element === element;
            });
            if (img_exists.length > 0) {
                let double_drops_exists = img_exists[0].images.hasOwnProperty("2x");
                return {[element]: {
                    path: double_drops_exists ? img_exists[0].images["2x"] : null}};
                }
                let any_double_drops = this.$props.rowdata.filter((v)=> { return v.images.hasOwnProperty("2x")});
                return {[element]: {path: any_double_drops.length > 0 ? 
                    any_double_drops[0].images["2x"] : 
                    this.$props.rowdata[0].images.path}};
        });
        let current_state = elements.map(element => {
            return { [element]: { "active": 0 }}
        });
        return {
            elements: elements,
            double_drops_images: Object.assign(...double_drops_images),
            default_images: Object.assign(...default_images),
            images: Object.assign(...JSON.parse(JSON.stringify(default_images))),
            current_state: Object.assign(...current_state),
            possible_states: ["", "void-select", "void-select void-double-drops"]
        };
    },
    methods: {
        toggle: function(element) {
            this.current_state[element]['active'] = 
                (1+this.current_state[element]['active']) % this.possible_states.length;
            if (this.possible_states[this.current_state[element]['active']].includes("void-double-drops")) {
                this.images[element].path = this.double_drops_images[element].path;
            } else {
                this.images[element].path = this.default_images[element].path;
            }
        }
    },
    /*template*/
    template:`
    <div class="row">
        <div class="col-2"></div>
        <div :class="'col-2 void '+possible_states[current_state[element]['active']]" v-for="element in elements" 
        :style="'background-image:url('+images[element].path+');'"
        v-on:click="toggle(element)">
        </div>
    </div>
    `
}));