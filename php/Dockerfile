FROM php:8.0.29-fpm-alpine3.16
COPY --from=composer:latest /usr/bin/composer /usr/local/bin/composer

RUN apk add --no-cache \
        libjpeg-turbo-dev \
        libpng-dev \
        libwebp-dev \
        libzip-dev \
        freetype-dev \
        autoconf \
        build-base
RUN pecl install redis
RUN docker-php-ext-install opcache sockets pcntl pdo pdo_mysql gd zip 
RUN docker-php-ext-enable redis
COPY php/production/opcache.ini /usr/local/etc/php/conf.d/opcache.ini

RUN apk add --no-cache \
        nano \
        sudo \
        bash
RUN adduser -D -u 1001 cart

USER cart

WORKDIR /opt/data

# RUN apk add --no-cache wget \
#     && wget https://static.x-cart.com/xc5kit/latest-auto.tgz \
#     && tar xvzf latest-auto.tgz