from flask_restx import fields, Model

from project.setup.api import api

error_api_model: Model = api.model('Сообщение об ошибке', {
    'message': fields.String(required=True, example='Error description'),
    'errors': fields.Wildcard(fields.String, required=False),
})
