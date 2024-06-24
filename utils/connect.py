from sqlalchemy import create_engine, sql

def create_server_connection(host, user_name, user_password,db):
  connection = None
  try:
    db_connect = create_engine('postgresql://'+user_name+':'+user_password+'@'+host+':5432/'+db)
    connection = db_connect.connect()
    print("PostgreSQL Database "+db+" connection successful")
  except Error as err:
    print(f"Error: '{err}'")
    
  return connection