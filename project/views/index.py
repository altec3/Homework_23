from flask_restx import Namespace, Resource

from project.setup.api.parsers import input_query

api = Namespace('/')


@api.route("/perform_query")
class QueriesResource(Resource):

    @api.expect(input_query)  # <-- from Frontend
    def post(self):
        """___"""
        payload = input_query.parse_args()
        print(payload)
