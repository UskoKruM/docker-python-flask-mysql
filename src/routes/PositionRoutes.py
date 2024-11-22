# Imports
from flask import Blueprint

# Exception Handler
from src.utils.ExceptionHandler import ExceptionHandler

# Response Methods
from .utils.ResponseMethods import ResponseMethods

# Services
from src.services.PositionService import PositionService


main = Blueprint('position_blueprint', __name__)


@main.route('/')
def get_positions():
    try:
        positions = PositionService.get_positions()

        if positions != None:
            if len(positions) > 0:
                return ResponseMethods.get_response_successful({'body': positions})
            else:
                return ResponseMethods.get_response_successful_notfound()
        else:
            return ResponseMethods.get_response_with_status_code(500)
    except Exception as ex:
        ExceptionHandler.log_exception(ex)
        return ResponseMethods.get_response_with_status_code(500)
