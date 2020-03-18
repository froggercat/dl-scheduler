import Vue from 'https://cdn.jsdelivr.net/npm/vue@latest/dist/vue.esm.browser.js'
import navbar from './components/navbar.js';
import voidscheduleinputday from './components/void-schedule-input-day.js'

var app = new Vue({
  el: '#app',
  data: {
    message: 'Hello Void!',
    routes: [
      { 'id': 'home', 'title': 'Home', 'route': 'index.html', 'active': '' },
      { 'id': 'void', 'title': 'Void Scheduler', 'route': 'void_scheduler.html', 'active': 'active' }
    ],
    days: [
      { "name": "Monday", "active": "active" }, 
      { "name": "Tuesday", "active": "" }, 
      { "name": "Wednesday", "active": "" }, 
      { "name": "Thursday", "active": "" }, 
      { "name": "Friday", "active": "" }, 
      { "name": "Saturday", "active": "" }, 
      { "name": "Sunday", "active": "" }]
  },
  components: {
    'navbar': navbar,
    'void-schedule-input-day': voidscheduleinputday
  },
  /*template*/
  template: `
    <div>
      <navbar :routes="routes"></navbar>
      <div id="carouselExampleIndicators" class="carousel slide" data-interval="false">
      <ol class="carousel-indicators">
        <li v-for="(day, index) in days" data-target="#carouselExampleIndicators" 
        :data-slide-to="index" :class="day.active"></li>
      </ol>
        <div class="carousel-inner"> 
          <div v-for="day in days" :class="'carousel-item '+day.active">
            <div class="container">
              <div class="jumbotron text-center">
                  <h1>{{ day.name }}</h1>
                  <void-schedule-input-day></void-schedule-input-day>
              </div>
            </div>
          </div>
        </div>
        <a class="carousel-control-prev" href="#carouselExampleIndicators" role="button" data-slide="prev">
          <span class="carousel-control-prev-icon" aria-hidden="true"></span>
          <span class="sr-only">Previous</span>
        </a>
        <a class="carousel-control-next" href="#carouselExampleIndicators" role="button" data-slide="next">
          <span class="carousel-control-next-icon" aria-hidden="true"></span>
          <span class="sr-only">Next</span>
        </a>
      </div>
    </div>
    `
})