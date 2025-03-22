import traceback, logging
from sys import stdout

class MyException(Exception):

    def __init__(self, message=None):
        self.message = message
        self.info = traceback.format_exc()
        super().__init__(message)

        logging.basicConfig(level= logging.INFO, stream= stdout)
        logger = logging.getLogger(__name__)

        logger.error(self)

    def __str__(self):
        return f"{self.message}  {self.info}"

