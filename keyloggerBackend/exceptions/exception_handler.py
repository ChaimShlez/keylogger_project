import logging
from errors.erros_types import ErrorsTypes


class ErrorManager:
    def __init__(self, log_file="errors.log"):
        self.log_file = log_file
        logging.basicConfig(filename=self.log_file, level=logging.ERROR,
                            format="%(asctime)s - %(levelname)s - %(message)s")

    def handle_error(self, error_type: ErrorsTypes, raise_exception=False):


        error_data = {

            "code": error_type.code,
            "message": error_type.message
        }


        print(f"Error [{error_type.code}]: {error_type.message}")


        if error_type.loggable:
            self.log_error(error_type)


        if raise_exception:
            raise Exception(error_data)


        return error_data

    def log_error(self, error_type: ErrorsTypes):

        logging.error(f"Error [{error_type.code}]: {error_type.message}")
