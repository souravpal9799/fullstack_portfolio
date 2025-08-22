def get_custom_logs(log_directory):
    import os

    logs = []
    try:
        for filename in os.listdir(log_directory):
            if filename.endswith('.log'):
                with open(os.path.join(log_directory, filename), 'r') as file:
                    logs.append({
                        'filename': filename,
                        'content': file.readlines()
                    })
    except Exception as e:
        return {'error': str(e)}

    return logs