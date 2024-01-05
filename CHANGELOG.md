# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a
Changelog](https://keepachangelog.com/en/1.0.0/).

## [Unreleased]

### Added

- `django-debug-toolbar` package

### Changed

- Convert `SECRET_KEY` into a required env var
- Add `required: false` to `depends_on` in `docker-compose.yml` (requires Docker Compose v2.20.2+)

#### Languages and services

- Update `Python` to `3.12.1`
- Update `Node` to `20.6.1`
- Update `Postgres` to `16.1`
- Update `Redis` to `7.2.3`

#### Back-end dependencies

- Update `Django` to `5.0.1`
- Update `black` to `23.12.1`
- Update `celery` to `5.3.6`
- Update `django-debug-toolbar` to `4.2.0`
- Update `flake8` to `7.0.0`
- Update `gunicorn` to `21.2.0`
- Update `isort` to `5.13.2`
- Update `psycopg` to `3.1.16`
- Update `redis` to `5.0.1`
- Update `whitenoise` to `6.6.0`

#### Front-end dependencies

- Update `autoprefixer` to `10.4.16`
- Update `esbuild` to `0.19.11`
- Update `postcss-import` to `16.0.0`
- Update `postcss` to `8.4.33`
- Update `tailwindcss` to `3.4.0`

## [0.10.0] - 2023-05-13

### Added

- Ability to customize `UID` and `GID` if you're not using `1000:1000` (check the `.env.example` file)
- Output `docker compose logs` in CI for easier debugging
- `isort` to auto-sort Python imports and a new `./run isort` command
- `./run quality` to run `lint`, `isort` and `format` in 1 command

### Changed

- Reference `PORT` variable in the `docker-compose.yml` web service instead of hard coding `8000`
- Adjust Hadolint to exit > 0 if any style warnings are present
- Rename `esbuild.config.js` to `esbuild.config.mjs` and refactor config for esbuild 0.17+

#### Languages and services

- Update `Python` to `3.11.3`
- Update `Node` to `18.15.0`
- Update `Postgres` to `15.3`
- Update `Redis` to `7.0.11`

#### Back-end dependencies

- Replace `psycopg2` with `psycopg` (3.1.9)
- Update `Django` to `4.2.1`
- Update `flake8` to `6.0.0`
- Update `isort` to `5.12.1`
- Update `redis` to `4.5.5`
- Update `whitenoise` to `6.4.0`

#### Front-end dependencies

- Update `autoprefixer` to `10.4.14`
- Update `esbuild` to `0.17.19`
- Update `postcss-import` to `15.1.0`
- Update `postcss` to `8.4.23`
- Update `tailwindcss` to `3.3.2`

### Removed

- `set -o nounset` from `run` script since it's incompatible with Bash 3.2 (default on macOS)

### Fixed

- Ensure Flake8, Black and isort all use 79 as the max line length
- HTML templates not reloading in development by using `loaders` in `src/config/setting.py`

## [0.9.0] - 2022-09-09

### Added

- `set -o nounset` to `run` script to exit if there's any undefined variables
- Adjust `x-assets` to use a `stop_grace_period` of `0` for faster CTRL+c times in dev

### Changed

- Switch Docker Compose `env_file` to `environment` for `postgres` to avoid needless recreates on `.env` changes
- Replace override file with Docker Compose profiles for running specific services
- Update Github Actions to use Ubuntu 22.04
- Enable BuildKit by default in the `.env.example` file

#### Languages and services

- Update `Python` to `3.10.5`
- Update `Node` to `16.15.1`
- Update `PostgreSQL` to `14.5`
- Update `Redis` to `7.0.4`

#### Back-end dependencies

- Update `Django` to `4.1.0`
- Update `black` to `22.6.0`
- Update `flake8` to `5.0.4`
- Update `celery` to `5.2.7`
- Update `redis` to `4.3.4`
- Update `whitenoise` to `6.2.0`

#### Front-end dependencies

- Update `autoprefixer` to `10.4.8`
- Update `esbuild` to `0.15.2`
- Update `postcss` to `8.4.16`
- Update `tailwindcss` to `3.1.8`

### Removed

- Docker Compose `env_file` property for `redis` to avoid needless recreates on `.env` changes
- Drop support for Docker Compose v1 (mainly to use profiles in an optimal way, it's worth it!)

## [0.8.0] - 2022-05-15

### Added

- `yarn cache clean` after `yarn install` in `Dockerfile` (Hadolint warning)
- `--no-cache-dir` flag to `pip3 install` command in `bin/pip3-install` (Hadolint warning)
- [esbuild-copy-static-files](https://github.com/nickjj/esbuild-copy-static-files) plugin to drastically improve how static files are copied (check `assets/esbuild.config.js`)

### Changed

- Update Bash shebang to use `#!/usr/bin/env bash` in `pip3-install` and `docker-entrypoint-web`
- Refactor `/up/` endpoint into its own app and add `/up/databases` as a second URL

#### Languages and services

- Update `Python` to `3.10.4`
- Update `Node` to `16.14.2`
- Update `PostgreSQL` to `14.2`
- Update `Redis` to `7.0.0`

#### Back-end dependencies

- Update `Django` to `4.0.4`
- Update `black` to `22.3.0`
- Update `celery` to `5.2.6`
- Update `psycopg2` to `2.9.3`
- Update `redis` to `4.3.1`
- Update `whitenoise` to `6.1.0`

#### Front-end dependencies

- Update `autoprefixer` to `10.4.7`
- Update `esbuild` to `0.14.39`
- Update `postcss-import` to `14.1.0`
- Update `postcss` to `8.4.13`
- Update `tailwindcss` to `3.0.24`

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

[Unreleased]: https://github.com/nickjj/docker-django-example/compare/0.10.0...HEAD
[0.10.0]: https://github.com/nickjj/docker-django-example/compare/0.9.0...0.10.0
[0.9.0]: https://github.com/nickjj/docker-django-example/compare/0.8.0...0.9.0
[0.8.0]: https://github.com/nickjj/docker-django-example/compare/0.7.0...0.8.0
[0.7.0]: https://github.com/nickjj/docker-django-example/compare/0.6.0...0.7.0
[0.6.0]: https://github.com/nickjj/docker-django-example/compare/0.5.0...0.6.0
[0.5.0]: https://github.com/nickjj/docker-django-example/compare/0.4.0...0.5.0
[0.4.0]: https://github.com/nickjj/docker-django-example/compare/0.3.1...0.4.0
[0.3.1]: https://github.com/nickjj/docker-django-example/compare/0.3.0...0.3.1
[0.3.0]: https://github.com/nickjj/docker-django-example/compare/0.2.0...0.3.0
[0.2.0]: https://github.com/nickjj/docker-django-example/compare/0.1.0...0.2.0
[0.1.0]: https://github.com/nickjj/docker-django-example/releases/tag/0.1.0
