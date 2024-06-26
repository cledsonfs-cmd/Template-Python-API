from flask_restx import Resource, Namespace
# from config import api
from model.users import UserController
from dto.users_dto import user_payload, user_response, user_payload_update

ns_user = Namespace('users', description='users operations')

@ns_user.route('/all')
class UsersResource(Resource):
  @ns_user.doc('get_all_users')
  def get(self):
    """Obtém a lista de users"""
    return {
      "status_code":200,
      "msg": "Sucesso",
      "data": UserController.getAll()
      }
    
@ns_user.route('/<id>')
class UsersResourceId(Resource):
  @ns_user.doc('get_users')
  def get(self, id):
    """Obtém um user com base em um ID"""
    return {
      "status_code":200,
      "msg": "Sucesso",
      "data": UserController.getId(id)
      }

@ns_user.route("/")
class UserPost(Resource):
    @ns_user.doc("post_a_user")    
    @ns_user.expect(user_payload)
    @ns_user.marshal_with(user_response)
    def post(self):
      """Cria um user"""
      return {"status_code": 200, "msg": "Sucesso", "data": UserController.save(ns_user.payload["email"], ns_user.payload["password"], ns_user.payload["status"], ns_user.payload["role"])}        

@ns_user.route("/update")
class UserPut(Resource):
    @ns_user.doc("put_a_user")    
    @ns_user.expect(user_payload_update)
    @ns_user.marshal_with(user_response)
    def put(self):
      """Atualiza um user"""
      return {"status_code": 200, "msg": "Sucesso", "data": UserController.update(ns_user.payload["id"],ns_user.payload["email"], ns_user.payload["password"], ns_user.payload["status"], ns_user.payload["role"])}   
    
@ns_user.route('/delete/<id>')
class UsersDelete(Resource):
  @ns_user.doc('delete_user')
  def delete(self, id):
    """Exlui um user"""
    return {
      "status_code":200,
      "msg": "Sucesso",
      "data": UserController.delete(id)
      }     