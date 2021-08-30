import ContactMe from './components/ContactMe.vue'
import Resume from './components/Resume.vue'
import Article from './components/Article.vue'
 



const routes = [
    { path: '/', component: Article },
    { path: '/resume', component: Resume },
    { path: '/contact-me', component: ContactMe }, 
  ]
  
  export default routes