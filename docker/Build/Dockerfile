FROM node:23-alpine3.20

LABEL maintainer="andre"

HEALTHCHECK CMD \
    curl -sf http://localhost:5000/ || exit 1

VOLUME [ "/var/nodeapp" ]

RUN adduser -h /var/nodeapp \
    -s /bin/bash \
    -D nodeapp && \
  apk add curl

WORKDIR /var/nodeapp

COPY app.js .
RUN chown nodeapp:nodeapp app.js

ARG VERSION
ENV VERSION=${VERSION:-1.0.0}

USER nodeapp
ENTRYPOINT [ "node" ]
CMD [ "app.js" ]