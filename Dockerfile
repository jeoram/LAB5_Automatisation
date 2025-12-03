FROM python:3.11

RUN mkdir /opt/hello_world/
WORKDIR /opt/hello_world/

COPY requirements.txt .
COPY COPY . /opt/hello_world/

EXPOSE 80

CMD [ "./hello_world" ]
