FROM python:3.9.6
RUN mkdir /usr/src/app
WORKDIR /usr/src/app
COPY ./requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["python", "main:app", "--host", "0.0.0.0", "--port", "8000"]