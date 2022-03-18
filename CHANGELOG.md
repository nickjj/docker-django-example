# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a
Changelog](https://keepachangelog.com/en/1.0.0/).

## [Unreleased]

### Added

- `yarn cache clean` after `yarn install` in `Dockerfile` (Hadolint warning)
- `--no-cache-dir` flag to `pip3 install` command in `bin/pip3-install` (Hadolint warning)
- [esbuild-copy-static-files](https://github.com/nickjj/esbuild-copy-static-files) plugin to drastically improve how static files are copied (check `assets/esbuild.config.js`)

### Changed

- Update Bash shebang to use `#!/usr/bin/env bash` in `pip3-install` and `docker-entrypoint-web`
- Refactor `/up/` endpoint into its own app and add `/up/databases` as a second URL

#### Languages and services

- Update `Python` to `3.10.3`
- Update `Node` to `16.14.0`
- Update `PostgreSQL` to `14.2`

#### Back-end dependencies

- Update `Django` to `4.0.3`
- Update `black` to `22.1.0`
- Update `celery` to `5.2.3`
- Update `psycopg2` to `2.9.3`
- Update `redis` to `4.1.4`
- Update `whitenoise` to `6.0.0`

#### Front-end dependencies

- Update `autoprefixer` to `10.4.4`
- Update `esbuild` to `0.14.27`
- Update `postcss` to `8.4.12`
- Update `tailwindcss` to `3.0.23`

### Fixed

- `COPY --chown=node:node ../ ../` has been fixed to be `COPY --chown=node:node . ..`

## [0.7.0] - 2021-12-25

### Added

- `/node_modules/.bin` to `$PATH` to easier access Yarn installed binaries
- `yarn:build:js` and `yarn:build:css` run script commands

### Changed

- Update `assets/tailwind.config.js` based on the new TailwindCSS v3 defaults
- Replace all traces of Webpack with esbuild
- Move JS and CSS from `assets/app` to `assets/js` and `assets/css`
- Rename `webpack` Docker build stage to `assets`
- Copy all files into the `assets` build stage to simplify things
- Replace `cp -a` with `cp -r` in Docker entrypoint to make it easier to delete older assets
- Rename `run hadolint` to `run lint:dockerfile`
- Rename `run flake8` to `run lint`
- Rename `run black` to `run format`
- Rename `run bash` to `run shell`

#### Languages and services

- Update `Node` to `16.13.1`

#### Front-end packages

- Update `postcss` to `8.4.5`
- Update `tailwindcss` to `3.0.7`

### Removed

- Deleting old assets in the Docker entrypoint (it's best to handle this out of band in a cron job, etc.)

## [0.6.0] - 2021-12-07

### Added

- Lint Dockerfile with <https://github.com/hadolint/hadolint>
- `redis` package to fulfill Django 4.x's Redis cache back-end requirements

### Changed

- Update `assets/tailwind.config.js` based on the new TailwindCSS v3 defaults

#### Languages and services

- Update `Node` to `14.18.1`
- Update `PostgreSQL` to `14.1` and switch to Debian Bullseye Slim
- Update `Redis` to switch to Debian Bullseye Slim

#### Back-end packages

- Update `Django` to `4.0`
- Update `celery` to `5.2.1`
- Update `flake8` to `4.0.1`
- Update `psycopg2` to `2.9.2`
- Update `redis` to `4.0.2`

#### Front-end packages

- Update `@babel/core` to `7.16.0`
- Update `@babel/preset-env` to `7.16.4`
- Update `@babel/register` to `7.16.0`
- Update `autoprefixer` to `10.4.0`
- Update `babel-loader` to `8.2.3`
- Update `copy-webpack-plugin` to `10.0.0`
- Update `css-loader` to `6.5.1`
- Update `css-minimizer-webpack-plugin` to `3.2.0`
- Update `mini-css-extract-plugin` to `2.4.5`
- Update `postcss-loader` to `6.2.1`
- Update `postcss` to `8.4.3`
- Update `tailwindcss` to `2.2.19`
- Update `webpack-cli` to `4.9.1`
- Update `webpack` to `5.64.4`

### Removed

- `django-redis` package since Django 4.x supports using Redis as a cache back-end now

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

[Unreleased]: https://github.com/nickjj/docker-django-example/compare/0.7.0...HEAD
[0.7.0]: https://github.com/nickjj/docker-django-example/compare/0.6.0...0.7.0
[0.6.0]: https://github.com/nickjj/docker-django-example/compare/0.5.0...0.6.0
[0.5.0]: https://github.com/nickjj/docker-django-example/compare/0.4.0...0.5.0
[0.4.0]: https://github.com/nickjj/docker-django-example/compare/0.3.1...0.4.0
[0.3.1]: https://github.com/nickjj/docker-django-example/compare/0.3.0...0.3.1
[0.3.0]: https://github.com/nickjj/docker-django-example/compare/0.2.0...0.3.0
[0.2.0]: https://github.com/nickjj/docker-django-example/compare/0.1.0...0.2.0
[0.1.0]: https://github.com/nickjj/docker-django-example/releases/tag/0.1.0
