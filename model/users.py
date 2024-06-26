from sqlalchemy import create_engine, sql
from utils.connect import create_server_connection

from flask import jsonify


class UserController:
  
  def getAll():
    conn = create_server_connection('localhost', 'postgres', 'postgres', 'template_nest')
    sql_query = sql.text("select id||'' as id ,email, password, status, role from public.user")
    query = conn.execute(sql_query)
    result = [dict(zip(tuple(query.keys()), i)) for i in query.cursor]    
    return result
  
  def getId(id):
    conn = create_server_connection('localhost', 'postgres', 'postgres', 'template_nest')
    sql_query = sql.text("select id||'' as id ,email, password, status, role from public.user where id='"+id+"'")
    query = conn.execute(sql_query)
    result = [dict(zip(tuple(query.keys()), i)) for i in query.cursor]
    return result   
  
  def save(email, password,status,role):
    conn = create_server_connection('localhost', 'postgres', 'postgres', 'template_nest')
    
    sql_query = sql.text("INSERT INTO public.user (id, updated_at, email, password, status, role) "
                        +"VALUES(uuid_generate_v4(), now(),'{0}','{1}','{2}','{3}')".format(email, password,status,role))
    conn.execute(sql_query)
    conn.commit()
    
    sql_query = sql.text("select id||'' as id ,email, password, status, role from public.user order by id desc limit 1")
    query = conn.execute(sql_query)
    result = [dict(zip(tuple(query.keys()), i)) for i in query.cursor]
    return result 
  
  def update(id, email, password,status,role):
    conn = create_server_connection('localhost', 'postgres', 'postgres', 'template_nest')
    
    sql_query = sql.text("UPDATE public.user SET updated_at=now(), email ='" + email +"', password ='" + password + "', status='"+status+"', role='"+role+"'  WHERE id ='"+id+"' ")

    conn.execute(sql_query)
    conn.commit()

    sql_query = sql.text("select id||'' ,email, password, status, role from public.user where id='"+id+"' ")
    query = conn.execute(sql_query)
    result = [dict(zip(tuple(query.keys()), i)) for i in query.cursor]
    return result 
  
  def delete(id):
    conn = create_server_connection('localhost', 'postgres', 'postgres', 'template_nest')
    
    
    sql_query = sql.text("DELETE FROM public.user WHERE id='"+id+"' ")
    conn.execute(sql_query)
    conn.commit()
    
    return {"status": "success"}
  
