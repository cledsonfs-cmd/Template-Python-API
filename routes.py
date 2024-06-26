from flask import Flask, request
from model.users import UserController
from swagger.config import api
from swagger.users_doc import ns_user


app = Flask(__name__)

@app.route("/all", methods=["GET"])
def get_users():
  return {
    "status_code":200,
    "msg": "Sucesso",
    "data": UserController.getAll()
    }
  
@app.route("/<id>", methods=["GET"])
def get_id(id):
  return {
    "status_code":200,
    "msg": "Sucesso",
    "data": UserController.getId(id)
    }
  
@app.route("/", methods=["POST"])
def post():
  payload = request.json
  return  {
    "status_code":200,
    "msg": "Usuário Cadastrado Com Sucesso",
    "data": UserController.save(payload)
    }
  
@app.route("/", methods=["PUT"])
def put():
  payload = request.json
  return  {
    "status_code":200,
    "msg": "Usuário Atualizado Com Sucesso",
    "data": UserController.save(payload)
    }
  
@app.route("/delete/<id>", methods=["delete"])
def delete(id):  
  return  {
    "status_code":200,
    "msg": "Usuário Escluído Com Sucesso",
    "data": UserController.delete(id)
    }
   
    
api.init_app(app)
api.add_namespace(ns_user)