module.exports = {
  context: __dirname + "/frontapp",
  entry: "./app.js",

  output: {
    filename: "app.js",
    path: __dirname + "/frontdist",
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