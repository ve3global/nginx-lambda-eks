FROM nginx
COPY index.html /usr/share/nginx/html/index.html
COPY nginxapi.conf /etc/nginx/sites-available/
RUN rm /etc/nginx/conf.d/default.conf
RUN ln -s /etc/nginx/sites-available/nginxapi.conf /etc/nginx/conf.d/
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
