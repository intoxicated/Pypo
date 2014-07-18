"""
    Exception class 
"""

Error = {
    

}

class PypoException(Exception):
    """ base class """
    def __init__(self, msg, error):
        Exception.__init__(self, msg)
        self.error = error

class SizeException(PypoException):
    def __init__(self, msg, error):
        PypoException.__init__(self, msg, error)

class NotFoundException(PypoException):
    def __init__(self, msg, error, path):
        PypoException.__init__(self, msg, error)
        self.path = path

class OperationAbortException(PypoException):
    def __init__(self, msg, error, operation):
        PypoException.__init__(self, msg, error)
        self.operation = operation

