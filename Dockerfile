FROM python:3.7
RUN mkdir -p /var/www/html/gel_database
WORKDIR /var/www/html/gel_database
ADD . /var/www/html/gel_database
RUN pip install -r requirements.txt
RUN chmod +x ./start.sh
RUN ./start.sh
