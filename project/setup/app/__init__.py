from flask import Flask

from project.setup.api import api
from project.views import query_ns


def create_app():
    app = Flask(__name__)
    app.app_context().push()

    api.init_app(app)
    api.add_namespace(query_ns)

    return app
