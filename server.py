from flask import Flask
from flask_restplus import Api
from src.endpoints.nasa_endpoint import api as test_ns
from src.endpoints.magic_seaweed_endpoint import api as msw
from src.endpoints.get_resume import api as resume

app = Flask(__name__)
api = Api(app, version='1.0', title='PySwag API',
          description='Building an API, work in progress')

api.add_namespace(test_ns, path="/")
api.add_namespace(msw, path="/")
api.add_namespace(resume, path="/")

if __name__ == "__main__":
    app.run(debug=True, port=5000)
