from flask import Blueprint, jsonify, request
from services.apache import get_apache_logs
from services.nginx import get_nginx_logs
from services.mysql import get_mysql_logs
from services.mongodb import get_mongodb_logs
from services.custom import get_custom_logs

api = Blueprint('api', __name__)

@api.route('/api/health')
def health():
    return {"status": "ok"}

@api.route('/logs/apache', methods=['GET'])
def apache_logs():
    logs = get_apache_logs()
    return jsonify(logs)

@api.route('/logs/nginx', methods=['GET'])
def nginx_logs():
    logs = get_nginx_logs()
    return jsonify(logs)

@api.route('/logs/mysql', methods=['GET'])
def mysql_logs():
    logs = get_mysql_logs()
    return jsonify(logs)

@api.route('/logs/mongodb', methods=['GET'])
def mongodb_logs():
    logs = get_mongodb_logs()
    return jsonify(logs)

@api.route('/logs/custom', methods=['POST'])
def custom_logs():
    data = request.json
    log_directory = data.get('directory')
    logs = get_custom_logs(log_directory)
    return jsonify(logs) if logs else jsonify({"error": "No logs found"}), 404