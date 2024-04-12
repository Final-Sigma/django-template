const path = require('path');

module.exports = {
    mode: 'development',
    entry: './assets/js/index.js',
    output: {
        filename: 'app.js',
        path: path.resolve(__dirname, 'static')
    },
    // module: {
    //     rules: [
    //     // Babel loader, only needed if using typescript instead of javascript
    //       {
    //         test: /\.(j|t)s$/,
    //         use: [{ loader: "babel-loader" }],
    //       },
    //      // If ever including stylesheets inside the javascript.
    //       {
    //         test: /\.css$/i,
    //         use: ["style-loader", "css-loader"],
    //       },
    //     ],
    //   }
}