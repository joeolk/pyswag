from flask import request
from flask_restx import Namespace, Resource, fields, reqparse
from src.schemas import payload_validation_failure, internal_server_error, success_resp, futures_params
from src.code.futures import futures

api = Namespace("Futures", description="Futures Related Queries")

payload_val_failed = api.schema_model(
    "payload_val_failed", payload_validation_failure)
int_server_error = api.schema_model(
    "internal_server_error", internal_server_error)


@api.route("high_low")
@api.doc(params=futures_params)
class ClassRedditEndpoint(Resource):
    """   """
    @classmethod
    @api.response(400, "Payload error", payload_val_failed)
    @api.response(500, "Internal Server Error", int_server_error)
    # @api.expect(model, validate=True)
    def get(cls):
        """  """
        parser = reqparse.RequestParser()
        parser.add_argument("ticker_symbol", type=str, required=True)
        parser.add_argument("start_date", type=str, required=False)
        parser.add_argument("end_date", type=str, required=False)
        args = parser.parse_args()

        resp = futures.get_high_low(args)
        return resp
