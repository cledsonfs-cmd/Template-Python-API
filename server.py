from turtle import pd
from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from sqlalchemy import create_engine, sql
from json import loads
from utils.connect import create_server_connection
from controller.userController import UserController

app = Flask(__name__)
api = Api(app)


class Users(Resource):
  def get(self):
    return UserController.getAll().__dict__
    


  def post(self):
    # conn = create_server_connection('localhost', 'postgres', 'postgres', 'template_nest')
    # user = loads(request)
    
    # email = request.json['email']
    # password = request.json['password']
    # status = request.json['status']
    # role = request.json['role']
    
    # sql_query = sql.text("insert into user values(null, '{0}','{1}','{2}','{3}')".format(email, password,status,role))
    # conn.execute(sql_query)
    
    # sql_query = sql.text('select * from user order by id desc limit 1')
    # query = conn.execute(sql_query)
        
    # result = [dict(zip(tuple(query.keys()), i)) for i in query.cursor]
    return UserController.save();
    
    return jsonify(result)

  def put(self):
    conn = create_server_connection('localhost', 'postgres', 'postgres', 'template_nest')
    
    id = request.json['id']
    email = request.json['email']
    password = request.json['password']
    status = request.json['status']
    role = request.json['role']

    sql_query = sql.text("update user set email ='" + str(email) +"', password ='" + str(password) + "', status='"+status+"', role='"+role+"'  where id ='"+id+"' ")
    conn.execute(sql_query)

    sql_query = sql.text("select * from user where id='"+id+"' ")
    query = conn.execute(sql_query)
    result = [dict(zip(tuple(query.keys()), i)) for i in query.cursor]
    return jsonify(result)

class UserById(Resource):
  def delete(self, id):
    conn = create_server_connection('localhost', 'postgres', 'postgres', 'template_nest')
    
    sql_query = sql.text("delete from user where id='"+id+"' ")
    conn.execute(sql_query)
    
    return {"status": "success"}

  def get(self, id):
    conn = create_server_connection('localhost', 'postgres', 'postgres', 'template_nest')
    
    sql_query = sql.text("select * from user where id ='"+id+"' ")
    query = conn.execute(sql_query)
    
    result = [dict(zip(tuple(query.keys()), i)) for i in query.cursor]
    return jsonify(result)

api.add_resource(Users, '/users') 
api.add_resource(UserById, '/users/<id>') 

if __name__ == '__main__':
    app.run()
