from sqlalchemy import create_engine, sql

def create_server_connection():
  host = 'localhost'
  port = '5432'
  db = 'template_python'
  user_name = 'postgres'
  user_password = 'postgres'
  connection = None
  try:
    db_connect = create_engine(f"postgresql://{user_name}:{user_password}@{host}:{port}/{db}")
    connection = db_connect.connect()
  except Error as err:
    print(f"Error: '{err}'")
    
  return connection