import ContactMe from './components/ContactMe.vue'
import Resume from './components/Resume.vue'
import Article from './components/Article.vue'
 



const routes = [
    { path: '/', component: Article, meta: {title : 'Ihab Zeedia: Home Page'} },
    { path: '/resume', component: Resume, meta: {title : 'Ihab Zeedia: My Resume'} },
    { path: '/contact-me', component: ContactMe, meta: {title : 'Ihab Zeedia: Contact Me'} }, 
  ]
  
  
  export default routes