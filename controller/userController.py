from sqlalchemy import create_engine, sql
from utils.connect import create_server_connection
from model.user import User


class UserController:
  
  def getAll():
    conn = create_server_connection('localhost', 'postgres', 'postgres', 'template_nest')
    sql_query = sql.text("select id ,email, password, status, role from public.user")
    query = conn.execute(sql_query)
    result = [dict(zip(tuple(query.keys()), i)) for i in query.cursor][0]    
    user = User(str(result["id"]) ,result["email"], result["password"], result["status"], result["role"])
    return user    
  
  def save(user):
    print(user)


 
  