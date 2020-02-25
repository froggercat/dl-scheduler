import Vue from 'https://cdn.jsdelivr.net/npm/vue@latest/dist/vue.esm.browser.js'
import navbar from './components/navbar.js';
import assets from './assets.js';

var app = new Vue({
    el: '#app',
    data: {
      message: 'Hello Void!',
      routes: [
        {'id': 'home', 'title': 'Home', 'route': 'index.html', 'active': ''},
        {'id': 'void', 'title': 'Void Scheduler', 'route': 'void_scheduler.html', 'active': 'active'}
      ]
    },
    components: {
      'navbar': navbar
    },
    /*template*/
    template: `
    <div>
      <navbar :routes="routes"></navbar>
      <div class="container">
        <div class="jumbotron">
            <h1>{{ message }}</h1>
        </div>
      </div>
    </div>
    `
  })