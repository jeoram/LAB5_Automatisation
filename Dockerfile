FROM python:3.11

RUN mkdir /opt/hello_world/
WORKDIR /opt/hello_world/

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . /opt/hello_world/

EXPOSE 4049

CMD [ "python", "hello_world.py"]