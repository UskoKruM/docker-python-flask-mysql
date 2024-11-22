# Imports
from flask import Blueprint
import uuid

# Consts
from src.utils.consts import EMPTY_STRING


main = Blueprint('index_blueprint', __name__)


@main.route('/')
def index():
    return "Hello World! - {}".format(str(uuid.uuid4()))


@main.route('/favicon.ico')
def favicon():
    return EMPTY_STRING, 204