FROM ubuntu

WORKDIR /flask_docker
RUN apt-get update
#RUN apk add git gcc python3-dev gpgme-dev libc-dev
RUN apt-get install libmysqlclient-dev -y
COPY requirement.txt .
#RUN pip install libmysqlclient-dev
RUN apt-get install python3-pip -y
RUN pip3 install -r requirement.txt
COPY python_connect_mysql.py .
COPY  . .
EXPOSE 5011

CMD ["python3", "python_connect_mysql.py"]
