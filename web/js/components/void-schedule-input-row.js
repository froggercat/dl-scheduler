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
                return {[element]: {path: single_drops_exists ?
                    img_exists[0].images.path :
                    img_exists[0].images["2x"] }}
            }
            let non2xdrops = this.$props.rowdata.filter((v)=> { return v.images.hasOwnProperty("path")});
            return {[element]: {path: non2xdrops.length > 0 ? 
                non2xdrops[0].images.path : 
                this.$props.rowdata[0].images["2x"]}};
        });
        return {
            elements: elements,
            default_images: Object.assign(...default_images)
        };
    },
    /*template*/
    template:`
    <div class="row">
        <div class="col-2" v-for="element in elements">
            <img :src="default_images[element].path">
        </div>
    </div>
    `
}));