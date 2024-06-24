from turtle import pd
from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from sqlalchemy import create_engine, sql
from json import dumps

db_connect = create_engine('postgresql://postgres:postgres@localhost:5432/template_nest')
app = Flask(__name__)
api = Api(app)


class Users(Resource):
  def get(self):
    conn = db_connect.connect()
    sql_query = sql.text("select * from public.user")
    query = conn.execute(sql_query)
    
    result = [dict(zip(tuple(query.keys()), i)) for i in query.cursor]
    
    return jsonify(result)   


  def post(self):
    conn = db_connect.connect()            	
    email = request.json['email']
    password = request.json['password']
    status = request.json['status']
    role = request.json['role']
    
    sql_query = sql.text("insert into user values(null, '{0}','{1}','{2}','{3}')".format(email, password,status,role))
    conn.execute(sql_query)
    
    sql_query = sql.text('select * from user order by id desc limit 1')
    query = conn.execute(sql_query)
        
    result = [dict(zip(tuple(query.keys()), i)) for i in query.cursor]
    
    return jsonify(result)

  def put(self):
    conn = db_connect.connect()
    
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
    conn = db_connect.connect()
    
    sql_query = sql.text("delete from user where id='"+id+"' ")
    conn.execute(sql_query)
    
    return {"status": "success"}

  def get(self, id):
    conn = db_connect.connect()
    
    sql_query = sql.text("select * from user where id ='"+id+"' ")
    query = conn.execute(sql_query)
    
    result = [dict(zip(tuple(query.keys()), i)) for i in query.cursor]
    return jsonify(result)

api.add_resource(Users, '/users') 
api.add_resource(UserById, '/users/<id>') 

if __name__ == '__main__':
    app.run()
