const path = require('path');

module.exports = {
    mode: 'development',
    entry: './static/index.js',
    output: {
        filename: 'output.js',
        path: path.resolve(__dirname, 'static')
    }
}