FROM node:16-alpine

ARG STATIC

WORKDIR $STATIC

COPY . $STATIC

RUN npm install

RUN chmod +rwx -R $STATIC
