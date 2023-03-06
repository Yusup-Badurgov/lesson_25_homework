from flask import Blueprint, jsonify, request
from marshmallow import ValidationError
from processing import get_resault
from model import RequestSchema

query_blueprint = Blueprint('main', __name__)

FILE_NAME = 'data/apache_logs.txt'


@query_blueprint.route('/perform_query', methods=['POST'])
def perform_query():
    """
    Вьюшка получает обрабатывает POST запрос, в котором передаются словарь парных параметров:
    {cmd1: str,
    value1: str,
    cmd2: str,
    value2: str,
    file_name: str}

    cmd1, value1 -  параметры поиска
    cmd2, value2 - параметры сортировки
    file_name - файл, по которому осуществляется поиск
    """

    data = request.json
    try:
        check_data = RequestSchema().load(data)
    except ValidationError as error:
        return jsonify(error.messages), 400

    cmd = check_data.get('cmd1')
    value = check_data.get('value1')
    file_name = check_data.get('file_name')
    data = get_resault(cmd, value, file_name, None)

    cmd = check_data.get('cmd2')
    value = check_data.get('value2')
    file_name = check_data.get('file_name')
    result = get_resault(cmd, value, file_name, data)

    return jsonify(result)


@query_blueprint.route('/ping', methods=['GET'])
def ping():
    return 'pong'


