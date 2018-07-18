# !! Require build !!
# docker build -t reverseproxy

FROM nginx

COPY ./reverseProxy.conf /etc/nginx/conf.d/default.conf
CMD ["/usr/sbin/nginx", "-g", "daemon off;"]
