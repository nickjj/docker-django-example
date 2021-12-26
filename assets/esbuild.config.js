const fs = require('fs')
const path = require('path')
const esbuild = require('esbuild')

const copySource = './static'
const copyDest = '../../'

let minify = false
let sourcemap = true
let watch_fs = true

if (process.env.NODE_ENV === 'production') {
  minify = true
  sourcemap = false
  watch_fs = false
}

const watch = watch_fs && {
  onRebuild(error) {
    if (error) console.error('[watch] build failed', error)
    else console.log('[watch] build finished')
  },
}

let copy = {
  name: 'copy',
  setup(build) {
    build.onEnd(() => fs.cpSync(copySource, path.join(build.initialOptions.outfile, copyDest), {
      recursive: true,
      force: true,
      dereference: true,
      preserveTimestamps: true,
    }))
  },
}

esbuild.build({
  entryPoints: ['./js/app.js'],
  outfile: '../public/js/app.js',
  bundle: true,
  minify: minify,
  sourcemap: sourcemap,
  watch: watch,
  plugins: [copy],
})
