import os
import time

def read_log(file_path, lines=50):
    """Read last N lines from a log file"""
    try:
        with open(file_path, "r") as f:
            return "".join(f.readlines()[-lines:])
    except FileNotFoundError:
        return f"❌ Log file not found: {file_path}"
    except PermissionError:
        return f"⚠️ Permission denied: {file_path}"
