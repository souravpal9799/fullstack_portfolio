def get_mysql_logs(log_file_path):
    logs = []
    try:
        with open(log_file_path, 'r') as file:
            for line in file:
                logs.append(line.strip())
    except Exception as e:
        logs.append(f"Error reading MySQL logs: {str(e)}")
    return logs