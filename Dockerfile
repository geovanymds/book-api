FROM python:3.10.1-alpine3.15
RUN mkdir /usr/src/app
WORKDIR /usr/src/app
COPY ./requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD [ "python", "./main.py" ]