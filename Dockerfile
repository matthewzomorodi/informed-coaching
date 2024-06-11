FROM python:3.9.19-bookworm

# install apache
RUN apt update && apt install -y \
    apache2 \
    apache2-dev \
    apache2-utils \
    vim \
    && apt clean

# setup python virtual environment
RUN mkdir /usr/.virtualenvs && cd /usr/.virtualenvs && python -m venv ./informed-coaching
RUN /usr/.virtualenvs/informed-coaching/bin/pip install --upgrade pip

# create python virtual environment and install packages
COPY requirements.txt /opt
RUN /usr/.virtualenvs/informed-coaching/bin/pip install -r /opt/requirements.txt

# install mod-wsgi
ADD ./mod_wsgi-5.0.0.tar.gz /opt
RUN cd /opt/mod_wsgi-5.0.0 && \
    ./configure && \
    make && make install

# apache configuration
COPY apache2.conf /etc/apache2/apache2.conf
COPY sites-available/*.conf /etc/apache2/sites-available
COPY --chown=www-data:www-data app /usr/local/www/app

# set Django production environment
COPY --chown=www-data:www-data .env-production /usr/local/www/app/informedcoaching/.env

# collect static files
RUN /usr/.virtualenvs/informed-coaching/bin/python \
    /usr/local/www/app/manage.py collectstatic --noinput

EXPOSE 80

# enable site
RUN a2ensite informed-coaching.conf

CMD [ "apache2ctl", "-D", "FOREGROUND" ]