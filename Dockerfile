FROM python:3.10.14-alpine3.20
ADD . /code
WORKDIR /code
RUN pip install -r requirements.txt
CMD python app.py