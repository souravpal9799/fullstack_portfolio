from flask import Flask, request, jsonify, render_template
from services import system_logs, custom_logs

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/logs/<service>", methods=["GET"])
def get_logs(service):
    lines = int(request.args.get("lines", 50))
    log_type = request.args.get("type", "error")

    if service == "custom":
        name = request.args.get("name")
        logs = custom_logs.get_custom_log(name, lines)
    else:
        logs = system_logs.get_logs(service, log_type, lines)

    return jsonify({"logs": logs})

@app.route("/custom/add", methods=["POST"])
def add_custom():
    data = request.get_json()
    name = data.get("name")
    path = data.get("path")
    result = custom_logs.add_custom_log(name, path)
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True, port=5000)
