from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

agenda = [
    {
        "name": "Vinicius",
        "email": "vicnicius2009@gmail.com",
        "phone": "11900000000"
    }
]


class HealthCheck(Resource):
    def get(self):
        return {"Health check": "It's healthy!"}


class FlaskAgenda(Resource):
    def get(self, contact_id):
        if contact_id == "all":
            return agenda
        return agenda[int(contact_id)]

    def post(self, contact_id):
        if contact_id == "add":
            info = request.json
            agenda.append(info)
        return agenda, 201

    def put(self, contact_id):
        int_id = int(contact_id)
        info = request.json

        agenda[int_id] = info
        return agenda[int_id], 201

    def delete(self, contact_id):
        int_id = int(contact_id)
        agenda.pop(int_id)

        return agenda


api.add_resource(FlaskAgenda, "/agenda/<string:contact_id>")
api.add_resource(HealthCheck, '/health')

if __name__ == '__main__':
    app.run(debug=True)
