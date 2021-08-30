// vue.config.js
module.exports = {
    // options...
    devServer: {
        proxy: {
            '/api/*': {
                target: 'http://web:8000',
                "secure": false
            },
        },
    }
  }
  