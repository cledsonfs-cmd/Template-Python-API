from flask_restx import fields
from swagger.config import api

user_payload = api.model(
    "Payload",
    {
        "email": fields.String,
        "password": fields.String,
        "status": fields.String,
        "role": fields.String,
    },
)

user_payload_update = api.model(
    "Payload",
    {
        "id": fields.String,
        "email": fields.String,
        "password": fields.String,
        "status": fields.String,
        "role": fields.String,
    },
)

user_response = api.model(
    "Response",
    {
        "status_code": fields.Integer,
        "msg": fields.String,
        "data": fields.Nested(user_payload),
    },
)