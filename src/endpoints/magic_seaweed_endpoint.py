from flask import request
from flask_restplus import Namespace, Resource, fields, reqparse
from src.schemas import payload_validation_failure, internal_server_error, success_resp, earth_event_params
from src.code.magic_seaweed_wrapper import magic_seaweed

api = Namespace("Magic Seaweed", description="Magic Seaweed Surf Determiner")

payload_val_failed = api.schema_model(
    "payload_val_failed", payload_validation_failure)
int_server_error = api.schema_model(
    "internal_server_error", internal_server_error)


@api.route("do_i_surf")
@api.doc(params=earth_event_params)
class ClassRedditEndpoint(Resource):
    """   """
    @classmethod
    @api.response(400, "Payload error", payload_val_failed)
    @api.response(500, "Internal Server Error", int_server_error)
    # @api.expect(model, validate=True)
    def get(cls):
        """  """
        parser = reqparse.RequestParser()
        parser.add_argument("status", type=str, required=False)
        parser.add_argument("days", type=int, required=False)
        args = parser.parse_args()

        resp = magic_seaweed.do_i_surf_today(args)
        return resp
