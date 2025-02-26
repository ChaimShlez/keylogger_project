class ServerException(Exception):
    def __init__(self, error_type, message="",user_input=None, original_exception=None):
        self.error_type = error_type
        self.message = f"{error_type.message}: {message}"
        self.code = error_type.code
        self.user_input = f"{user_input}"
        self.original_exception = original_exception
        super().__init__(self.message)


