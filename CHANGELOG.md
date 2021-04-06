# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a
Changelog](https://keepachangelog.com/en/1.0.0/).

## [Unreleased]

- Nothing yet!

## [0.3.1] - 2021-04-06

### Fixed

- Use `DEFAULT_AUTO_FIELD` in `settings.py` instead of the lowercase variant

## [0.3.0] - 2021-04-06

### Changed

- Update Django to `3.2`
- Update TailwindCSS to `2.1.0` and enable the JIT compiler

### Removed

- Remove Webpack's cache since the JIT compiler is pretty speedy as is

## [0.2.0] - 2021-03-17

### Changed

- Replace `##` comments with `#` in the `run` script
- Switch `OptimizeCSSAssetsPlugin` with `CssMinimizerPlugin` for Webpack 5
- Replace deprecated Webpack 5 `file-loader` with `asset/resource`
- Update flake8 from `3.8.4` to `3.9.0`

### Removed

- Remove unnecessary `mkdir` for the pip cache dir and chown'ing a few directories
- Unused `webpack` import in Webpack config

### Fixed

- Make sure `public_collected/.keep` is never removed
- Code styling issues in the Webpack config (single quotes, semi-colons, etc.)

## [0.1.0] - 2021-02-24

### Added

- Everything!

[Unreleased]: https://github.com/nickjj/docker-django-example/compare/0.3.1...HEAD
[0.3.1]: https://github.com/nickjj/docker-django-example/compare/0.3.0...0.3.1
[0.3.0]: https://github.com/nickjj/docker-django-example/compare/0.2.0...0.3.0
[0.2.0]: https://github.com/nickjj/docker-django-example/compare/0.1.0...0.2.0
[0.1.0]: https://github.com/nickjj/docker-django-example/releases/tag/0.1.0
