from utils.log_reader import read_log

CUSTOM_LOGS = {}

def add_custom_log(name, path):
    CUSTOM_LOGS[name] = path
    return {"status": "added", "log": name, "path": path}

def get_custom_log(name, lines=50):
    if name in CUSTOM_LOGS:
        return read_log(CUSTOM_LOGS[name], lines)
    return f"❌ Custom log '{name}' not found"
