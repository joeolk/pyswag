from flask import Flask
from flask_restplus import Api
from src.endpoints.endpoint import api as test_ns

app = Flask(__name__)
api = Api(app, version='1.0', title='Test API', description='Building an API')

api.add_namespace(test_ns, path="/")

if __name__ == "__main__":
    app.run(debug=True, port=5000)
