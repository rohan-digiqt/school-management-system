def create_response(data, status, message):
    return {
        "status": status,
        "message": message,
        "data": data
    }