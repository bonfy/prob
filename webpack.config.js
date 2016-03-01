var webpack = require('webpack');
var path = require('path');

var PATHS = {
  app: path.join(__dirname, 'frontapp'),
  build: path.join(__dirname, 'frontdist'),
  entry: path.resolve(__dirname, 'frontapp/app.js')
};


config = {
  entry: PATHS.entry,
  output: {
    filename: "app.js",
    path: PATHS.build,
  },
  resolve: {
    extensions: ['', '.js', '.jsx']
  },
  module: {
  loaders: [
     {
        test: /\.js$/,
        exclude: /node_modules/,
        //loaders: ["babel-loader"],
        loader: 'babel-loader',
        query: {
          presets: ['es2015', 'react']
        }
      }
    ],
  },
}

module.exports = config;