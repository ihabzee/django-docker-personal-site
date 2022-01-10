// vue.config.js
const path = require('path'); 

module.exports = {
    // options... 
    css: {
        extract: {
            filename: 'css/[name].css',
            chunkFilename: 'css/[name].css',
        },
    },
    configureWebpack: {
        output: {
            filename: 'js/[name].js',
            chunkFilename: 'js/[name].js',
        }
    },
    devServer: {
        proxy: {
            '/api/*': {
                target: 'http://web:8000',
                "secure": false
            },
        },
        disableHostCheck : true
    },
      // outputDir must be added to Django's TEMPLATE_DIRS
  outputDir: '../dist/vue/', 
}
