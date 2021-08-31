// vue.config.js
const path = require('path'); 

module.exports = {
    // options... 
    devServer: {
        proxy: {
            '/api/*': {
                target: 'http://web:8000',
                "secure": false
            },
        },
    },
      // outputDir must be added to Django's TEMPLATE_DIRS
  outputDir: '../dist/vue/', 
}
