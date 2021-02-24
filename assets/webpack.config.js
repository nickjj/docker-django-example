var { merge } = require('webpack-merge');
var webpack = require('webpack');
var CopyWebpackPlugin = require('copy-webpack-plugin');
var MiniCssExtractPlugin = require('mini-css-extract-plugin');
var OptimizeCSSAssetsPlugin = require('optimize-css-assets-webpack-plugin');
var TerserPlugin = require('terser-webpack-plugin');

var node_modules_path = '/node_modules'

var common = {
  watchOptions: {
    poll: (process.env.WEBPACK_WATCHER_POLL || 'false') === 'true'
  },
  cache: {
    type: 'filesystem',
    cacheDirectory: __dirname + '/../.webpack_cache'
  },
  snapshot: {
    managedPaths: [node_modules_path]
  },
  module: {
    rules: [
      {
        test: /\.js$/,
        exclude: [`/${node_modules_path}/`],
        use: [
          {loader: "babel-loader"}
        ]
      },
      {
        test: [/\.css$/],
        use: [
          MiniCssExtractPlugin.loader,
          'css-loader',
          'postcss-loader'
        ]
      },
      {
        test: /\.(png|jpg|gif|svg)$/,
        exclude: /fonts/,
        use: [
          {loader: 'file-loader?name=/images/[name].[ext]'}
        ]
      },
      {
        test: /\.(ttf|eot|svg|woff2?)$/,
        exclude: /images/,
        use: [{
          loader: 'file-loader',
          options: {
            name: '[name].[ext]',
            outputPath: 'fonts/',
            publicPath: '../fonts'
          }
        }]
      }
    ]
  },
  optimization: {
    minimizer: [
      new TerserPlugin(),
      new OptimizeCSSAssetsPlugin({})
    ]
  }
};

module.exports = [
  merge(common, {
    entry: [
      __dirname + '/app/app.css',
      __dirname + '/app/app.js'
    ],
    output: {
      path: __dirname + '/../public',
      filename: 'js/app.js'
    },
    resolve: {
      modules: [
        node_modules_path,
        __dirname + '/app'
      ]
    },
    plugins: [
      new CopyWebpackPlugin({patterns: [{from: __dirname + '/static'}]}),
      new MiniCssExtractPlugin({filename: 'css/app.css'}),
    ]
  })
];
