<p align="center">
  <a href="https://www.python.org/" target="blank"><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Python-logo-notext.svg/1869px-Python-logo-notext.svg.png" width="200" alt="Python Logo" /></a>
</p>

## Description

[Template-Python-API](https://github.com/cledsonfs-cmd/Template-Python-API): Template para o desenvolvimento de APIs com base na linguagem Python.

## Technologies used
- [Python 3.11](https://www.python.org/)
- [Django REST framework 3.15](https://www.django-rest-framework.org/tutorial/quickstart/)
- [dj-rest-auth 6](https://dj-rest-auth.readthedocs.io/en/latest/installation.html)
- [django-allauth 0.66](https://docs.allauth.org/en/latest/installation/quickstart.html)


## Installation

```bash
$ pip install virtualenv
```
```bash
$ python3 -m venv env
```
```bash
$ source env/bin/activate
```
```bash
$ pip install -r requirements.txt
```
```bash
$ python3 manage.py makemigrations
```
```bash
$ python3 manage.py migrate
```

## Running the app

```bash
# run
$ python3 manage.py runserver
```
### Documentation
- Django REST framework: [http://http://127.0.0.1:8000/](http://localhost:8000)
- Django Admin: [http://http://127.0.0.1:8000/admin](http://localhost:8000/admin)
  * User: admn
  * Password: admn123456
## Docker

```bash
$ docker compose up -d --build
```

## Stay in touch

- Author - [Cledson Francisco Silva](https://www.linkedin.com/in/cledson-francisco-silva-32737a2a/)
- E-mail - [cledsonfs@gmail.com](mailto:cledsonfs@gmail.com)
