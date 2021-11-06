# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a
Changelog](https://keepachangelog.com/en/1.0.0/).

## [Unreleased]

### Changed

#### Languages and services

- Update `Node` to `14.18.1`

#### Back-end packages

- Update `Django` to `3.2.9`
- Update `flake8` to `4.0.1`

#### Front-end packages

- Update `@babel/core` to `7.16.0`
- Update `@babel/preset-env` to `7.16.0`
- Update `@babel/register` to `7.16.0`
- Update `autoprefixer` to `10.4.0`
- Update `babel-loader` to `8.2.3`
- Update `css-loader` to `6.5.1`
- Update `mini-css-extract-plugin` to `2.4.4`
- Update `postcss-loader` to `6.2.0`
- Update `postcss` to `8.3.11`
- Update `tailwindcss` to `2.2.19`
- Update `webpack-cli` to `4.9.1`
- Update `webpack` to `5.62.1`

### Added

- Lint Dockerfile with <https://github.com/hadolint/hadolint>

## [0.5.0] - 2021-10-10

### Changed

#### Languages and services

- Update `Python` to `3.10.0` and switch to Debian Bullseye Slim
- Update `PostgreSQL` to `14.0`
- Update `Redis` to `6.2.6`

#### Back-end packages

- Update `Django` to `3.2.8`
- Update `celery` to `5.1.2`
- Update `psycopg2` to `2.9.1`
- Update `whitenoise` to `5.3.0`

#### Front-end packages

- Update `@babel/core` to `7.15.8`
- Update `@babel/preset-env` to `7.15.8`
- Update `@babel/register` to `7.15.3`
- Update `autoprefixer` to `10.3.7`
- Update `copy-webpack-plugin` to `9.0.1`
- Update `css-loader` to `6.4.0`
- Update `css-minimizer-webpack-plugin` to `3.1.1`
- Update `mini-css-extract-plugin` to `2.4.2`
- Update `postcss-loader` to `6.1.1`
- Update `postcss` to `8.3.9`
- Update `tailwindcss` to `2.2.16`
- Update `webpack-cli` to `4.9.0`
- Update `webpack` to `5.58.1`

## [0.4.0] - 2021-06-11

### Added

- `bin/rename-project` script to assist with renaming the project
- Use Black to format Python code
- Set `PYTHONPATH="."` in the Dockerfile

### Changed

- Rename `src/hello/` directory to `src/config/` to be more portable
- Replace `APP_NAME` in `run` script with `POSTGRES_USER` for connecting to psql
- Avoid using multi-line imports with commas or parenthesis
- Update Python from `3.9.2` to `3.9.5`
- Update PostgreSQL from `13.2` to `13.3`
- Update Redis from `6.0.10` to `6.2.4`
- Update Tailwind from `2.1.0` to `2.1.2`
- Update Django from `3.2` to `3.2.4`
- Update django-redis from `4.12.1` to `5.0.0`
- Update Celery from `5.0.5` to `5.1.0`
- Update flake8 from `3.9.0` to `3.9.2`
- Update all Webpack related dependencies to their latest versions
- Use the Docker Compose spec in `docker-compose.yml` (removes `version:` property)

### Fixed

- Set an empty ENTRYPOINT for the worker to avoid race conditions when copying static files
- Fix `run` script error for unbound variable in older versions of Bash on macOS
- Potential issue on Mac M1s by adding `depends_on` to Webpack service

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

[Unreleased]: https://github.com/nickjj/docker-django-example/compare/0.5.0...HEAD
[0.5.0]: https://github.com/nickjj/docker-django-example/compare/0.4.0...0.5.0
[0.4.0]: https://github.com/nickjj/docker-django-example/compare/0.3.1...0.4.0
[0.3.1]: https://github.com/nickjj/docker-django-example/compare/0.3.0...0.3.1
[0.3.0]: https://github.com/nickjj/docker-django-example/compare/0.2.0...0.3.0
[0.2.0]: https://github.com/nickjj/docker-django-example/compare/0.1.0...0.2.0
[0.1.0]: https://github.com/nickjj/docker-django-example/releases/tag/0.1.0
