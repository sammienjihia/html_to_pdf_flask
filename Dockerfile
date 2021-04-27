FROM python:3.8-buster

RUN apt-get -y update \
    && apt-get install -y \
        fonts-font-awesome \
        libffi-dev \
        libgdk-pixbuf2.0-0 \
        libpango1.0-0 \
        python-dev \
        python-lxml \
        shared-mime-info \
        libcairo2 \
        wkhtmltopdf \
    && apt-get -y clean
# COPY requirements.txt /usr/data
RUN pip install Flask
RUN pip install WeasyPrint
RUN pip install Flask-WeasyPrint
RUN pip install pdfkit

ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
EXPOSE 5000

COPY . /usr/src/app
WORKDIR /usr/src/app

CMD ["flask", "run"]

