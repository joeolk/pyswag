from flask import request
from flask_restplus import Namespace, Resource, fields, reqparse
from src.schemas import payload_validation_failure, internal_server_error, success_resp, earth_event_params
from src.code.nasa_wrapper import nasa_wrapper

api = Namespace("NASA", description="NASA Wrapper")

# model = api.model(
#     "Test endpoint",
#     {
#         "test_param": fields.String(
#             required=True,
#             description="test parametere for endpoint",
#             help="Cannot be blank and must be data type string."
#         )
#     }
# )

payload_val_failed = api.schema_model(
    "payload_val_failed", payload_validation_failure)
int_server_error = api.schema_model(
    "internal_server_error", internal_server_error)


@api.route("earth_events")
@api.doc(params=earth_event_params)
class ClassRedditEndpoint(Resource):
    """ NASA Events wrapper endpoint """
    @classmethod
    @api.response(400, "Payload error", payload_val_failed)
    @api.response(500, "Internal Server Error", int_server_error)
    # @api.expect(model, validate=True)
    def get(cls):
        """  """
        parser = reqparse.RequestParser()
        parser.add_argument("status", type=str, required=False)
        parser.add_argument("days", type=int, required=False)
        parser.add_argument("category", type=str, required=False)
        args = parser.parse_args()

        resp = nasa_wrapper.get_earth_events(args)
        return resp
