FROM python:2.7.14-alpine3.7
MAINTAINER Brandon Gulla im@brandongulla.com
RUN mkdir /src
COPY secrets.env /src
COPY app.py /src
COPY notify.py /src
COPY requirements.txt /src
WORKDIR "/src"
RUN pip install -r requirements.txt
CMD ["python","app.py"]