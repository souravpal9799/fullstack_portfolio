def get_apache_logs(log_file_path):
    logs = []
    try:
        with open(log_file_path, 'r') as file:
            for line in file:
                logs.append(line.strip())
    except Exception as e:
        logs.append(f"Error reading log file: {str(e)}")
    return logs