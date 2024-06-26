from turtle import pd
from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from sqlalchemy import create_engine, sql
from json import loads
from utils.connect import create_server_connection
from controller.userController import UserController
from model.user import User

app = Flask(__name__)
api = Api(app)


class Users(Resource):
  
  @app.route('/users')
  def getall():
    return jsonify(UserController.getAll()) 
  
  @app.route('/users/<id>')
  def getid(id):    
    return jsonify(UserController.getId(id))
  
  @app.route('/users', methods=['POST'])
  def post():      
    return jsonify(UserController.save(request.json['email'], request.json['password'],
                               request.json['status'],request.json['role']))
  
  @app.route('/users', methods=['PUT'])  
  def put():
    return jsonify(UserController.update(request.json['id'], request.json['email'], 
                                 request.json['password'],request.json['status'],
                                 request.json['role']))
  
  @app.route('/users/<id>', methods=['DELETE'])
  def delete(id):    
    return UserController.delete(id)

if __name__ == '__main__':
    app.run()
