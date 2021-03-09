# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a
Changelog](https://keepachangelog.com/en/1.0.0/).

## [Unreleased]

### Changed

- Replace `##` comments with `#` in the `run` script
- Switch `OptimizeCSSAssetsPlugin` with `CssMinimizerPlugin` for Webpack 5

### Removed

- Remove unnecessary `mkdir` for the pip cache dir and chown'ing a few directories

### Fixed

- Make sure `public_collected/.keep` is never removed

## [0.1.0] - 2021-02-24

### Added

- Everything!

[0.1.0]: https://github.com/nickjj/docker-django-example/releases/tag/0.1.0
