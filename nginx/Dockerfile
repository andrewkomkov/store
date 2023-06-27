FROM nginx:alpine
RUN apk add certbot certbot-nginx bash wget sudo
ADD nginx/default.conf /etc/nginx/conf.d

# certbot --nginx -d yourdomain.com
RUN adduser -D -u 1001 cart
# USER cart

WORKDIR /etc/nginx/