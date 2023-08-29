import Vue from 'vue'
import VueRouter from 'vue-router'
import LoginView from '@/views/LoginView.vue'
import HomeView from '@/views/HomeView.vue'
// import BookingsView from '@/views/BookingsView.vue'
// import HomeView from '@/views/HomeView.vue'
//import ProfileView from '@/views/ProfileView.vue'
// import SignUpView from '@/views/SignUpView.vue'


Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'login',
    component: LoginView
  },
  {
    path: '/home',
    name: 'home',
    component: HomeView
  },
  // {
  //   path: '/bookings',
  //   name: 'bookings',
  //   component: BookingsView
  // },
  // {
  //   path: '/admin',
  //   name: 'admin',
  //   component: AdminView,
  //   children:[
  //     {
  //       path:'',
  //       name:'dashboard',
  //       component : () => import('../components/AdminMoviesComp.vue')
  //     },
  //     {
  //       path:'dashboard',
  //       name:'dashboard',
  //       component : () => import('../components/AdminMoviesComp.vue')
  //     },
  //     {
  //       path:'report',
  //       name:'report',
  //       component:() => import ('../components/AdminReportComp.vue')
  //     }
  //   ]
  // },
  // {
  //   path: '/home',
  //   component: HomeView,
    // children: [
    //   {
    //     path: '',
    //     component: () => import(/* webpackChunkName: "about" */ '../components/FeedComponent.vue')
    //   },
      // {
      //   path: 'liked-posts',
      //   component: LikedPostsComponent
      // },
      // {
      //   path: 'people',
      //   component: () => import(/* webpackChunkName: "about" */ '../components/PeopleComponent.vue')
      // },
      // {
      //   path: 'bookmarks',
      //   component: () => import(/* webpackChunkName: "about" */ '../components/BookmarksComponent.vue')
      // }
    //]
  // },
  // {
  //   path: '/profile/:id',
  //   name: 'user-profile',
  //   component: () => import(/* webpackChunkName: "about" */ '../views/ProfileView.vue')
  // }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
