FROM python:3

RUN mkdir /code
WORKDIR /code

COPY requirements.txt .

#RUN pip install --upgrade pip

RUN pip3 install -r requirements.txt

COPY . .

# Define as variáveis de ambiente HOST e PORT
ENV HOST=0.0.0.0
ENV PORT=5000

EXPOSE 5000

CMD [ "python3", "run.py" ]