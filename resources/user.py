import sqlite3
from flask_restful import Resource, reqparse
from models.user import UserModel

class RegisterUser(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument("username",
        type=str,
        required = True,
        help = "This field cannot be blank."
    )
    parser.add_argument("password",
        type=str,
        required = True,
        help = "This field cannot be blank."
    )

    def post(self):
        data = RegisterUser.parser.parse_args()

        if UserModel.findByUsername(data["username"]):
            return {"message":"A user with that username already exists!"}, 400

        user = UserModel(data['username'], data['password'])
        user.save_to_db()

        return {"message": "User registered successfully."}, 201
