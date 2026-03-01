from src.core.response_code import ResponseCode


class APIContract:
    @staticmethod
    def success(data):
        return {
            "status": "success",
            "code": ResponseCode.SUCCESS,
            "data": data,
            "message": "success"
        }

    @staticmethod
    def error(status_code, message):
        return {
            "status": "error",
            "code": status_code,
            "message": message,
        }
