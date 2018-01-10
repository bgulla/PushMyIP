FROM python:2.7.14-alpine3.7
MAINTAINER Brandon Gulla im@brandongulla.com

COPY . /src
WORKDIR "/src"
RUN pip install -r requirements.txt
CMD ["python","app.py"]