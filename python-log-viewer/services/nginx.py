def get_nginx_logs(log_file_path):
    logs = []
    try:
        with open(log_file_path, 'r') as file:
            for line in file:
                # Process each line of the log file
                logs.append(line.strip())
    except Exception as e:
        # Handle exceptions (e.g., file not found, permission denied)
        logs.append(f"Error reading Nginx logs: {str(e)}")
    return logs