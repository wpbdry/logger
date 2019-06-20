import logging


class Logger():
    loggers = {}
    def __init__(self, name, file_name_prefix, levels):
        for level in levels:
            self.loggers[level] = logging.getLogger(f'{name}_{level}')
            handler = logging.FileHandler(f'{file_name_prefix}{level}')
            handler.setLevel(logging.DEBUG)
            self.loggers[level].addHandler(handler)
        
    def debug(self, message):
        self.loggers['DEBUG'].debug(message)
    
    def info(self, message):
        self.loggers['INFO'].info(message)
    
    def warning(self, message):
        self.loggers['WARNING'].warning(message)
    
    def error(self, message):
        self.loggers['ERROR'].error(message)
    
    def critical(self, message):
        self.loggers['CRITICAL'].critical(message)


# class Handler(logging.FileHandler):
#     def __init__(self, name):
#         if name != 'DEBUG' and name != 'INFO' and name != 'WARNING' and name != 'ERROR' and name != 'CRITICAL':
#             raise InvalidName()
#         super().__init__(f'{prefix}{name}.log')
#         print(name)
#         self.setLevel(eval(name))


class InvalidName(Exception):
    def __init__(
        self,
        message = "name must be one of DEBUG, INFO, WARNING, ERROR, or CRITICAL",
        errors=None):
        super().__init__(message)

        if errors:
            self.errors = errors
