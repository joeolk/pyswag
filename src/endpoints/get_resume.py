from flask import request
from flask_restplus import Namespace, Resource, fields, reqparse
from src.schemas import payload_validation_failure, internal_server_error
from src.code.resume import get_resume

api = Namespace("JOResume", description="Get Joe's Resume")

payload_val_failed = api.schema_model(
    "payload_val_failed", payload_validation_failure)
int_server_error = api.schema_model(
    "internal_server_error", internal_server_error)


@api.route("resume")
class ClassResumeEndpoint(Resource):
    """   """
    @classmethod
    @api.response(400, "Payload error", payload_val_failed)
    @api.response(500, "Internal Server Error", int_server_error)
    def get(cls):
        """  """
        resp = get_resume.get_resume()
        return resp
