
FROM continuumio/anaconda3
EXPOSE 8000
RUN apt-get update && apt-get install -y apache2 \
    apache2-dev \   
    vim \
 && apt-get clean \
 && apt-get autoremove \
 && rm -rf /var/lib/apt/lists/*
WORKDIR /var/www/nlp_api/
COPY ./nlp_api.wsgi /var/www/nlp_api/nlp_api.wsgi
COPY ./nlp_api.py /var/www/nlp_api/nlp_api.py
COPY ./requirement.txt /var/www/nlp_api/requirement.txt
RUN pip install -r requirement.txt
RUN /opt/conda/bin/mod_wsgi-express install-module
RUN mod_wsgi-express setup-server nlp_api.wsgi --port=8000 \
    --user www-data --group www-data \
    --server-root=/etc/mod_wsgi-express-80
CMD /etc/mod_wsgi-express-80/apachectl start -D FOREGROUND