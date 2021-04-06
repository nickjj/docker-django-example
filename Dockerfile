FROM node:14.15.5-buster-slim AS webpack
LABEL maintainer="Nick Janetakis <nick.janetakis@gmail.com>"

WORKDIR /app/assets

RUN apt-get update \
  && apt-get install -y build-essential curl libpq-dev --no-install-recommends \
  && rm -rf /var/lib/apt/lists/* /usr/share/doc /usr/share/man \
  && apt-get clean \
  && mkdir -p /node_modules && chown node:node -R /node_modules /app

USER node

COPY --chown=node:node assets/package.json assets/*yarn* ./

RUN yarn install

ARG NODE_ENV="production"
ENV NODE_ENV="${NODE_ENV}" \
    USER="node"

COPY --chown=node:node assets .

# We need to copy the main web app so that PurgeCSS can find our HTML templates
# at build time so it knows what to purge / keep in the final CSS bundle.
#
# This doesn't bloat anything in the end because only the final assets get
# copied over in another build stage. Yay for multi-stage builds!
COPY --chown=node:node src /app/src

RUN if [ "${NODE_ENV}" != "development" ]; then \
  yarn run build; else mkdir -p /app/public; fi

CMD ["bash"]

#

FROM python:3.9.2-slim-buster AS app
LABEL maintainer="Nick Janetakis <nick.janetakis@gmail.com>"

WORKDIR /app

RUN apt-get update \
  && apt-get install -y build-essential curl libpq-dev --no-install-recommends \
  && rm -rf /var/lib/apt/lists/* /usr/share/doc /usr/share/man \
  && apt-get clean \
  && useradd --create-home python \
  && mkdir -p /public_collected public \
  && chown python:python -R /public_collected /app

USER python

COPY --chown=python:python requirements*.txt ./
COPY --chown=python:python bin/ ./bin

RUN chmod 0755 bin/* && bin/pip3-install

ARG DEBUG="false"
ENV DEBUG="${DEBUG}" \
    PYTHONUNBUFFERED="true" \
    PATH="${PATH}:/home/python/.local/bin" \
    USER="python"

COPY --chown=python:python --from=webpack /app/public /public
COPY --chown=python:python . .

WORKDIR /app/src

RUN if [ "${DEBUG}" = "false" ]; then \
  SECRET_KEY=dummyvalue python3 manage.py collectstatic --no-input; \
    else mkdir -p /app/public_collected; fi

ENTRYPOINT ["/app/bin/docker-entrypoint-web"]

EXPOSE 8000

CMD ["gunicorn", "-c", "python:config.gunicorn", "config.wsgi"]
