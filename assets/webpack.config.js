var { merge } = require('webpack-merge');
var webpack = require('webpack');
var CopyWebpackPlugin = require('copy-webpack-plugin');
var MiniCssExtractPlugin = require('mini-css-extract-plugin');
var CssMinimizerPlugin = require('css-minimizer-webpack-plugin');
var TerserPlugin = require('terser-webpack-plugin');

var node_modules_path = '/node_modules';

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
          {loader: 'babel-loader'}
        ]
      },
      {
        test: /\.css$/,
        use: [
          MiniCssExtractPlugin.loader,
          'css-loader',
          'postcss-loader'
        ]
      },
      {
        test: /\.(png|svg|jpg|jpeg|gif)$/i,
        type: 'asset/resource',
      },
      {
        test: /\.(woff|woff2|eot|ttf|otf)$/i,
        type: 'asset/resource',
        generator: {
          filename: 'fonts/[name][ext]'
        }
      },
    ]
  },
  optimization: {
    minimizer: [
      new TerserPlugin(),
      new CssMinimizerPlugin({})
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
      filename: 'js/app.js',
      publicPath: '/'
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
