"""
    Exception class 
"""

Error = {
    

}

class PypoException(Exception):
    """ base class """
    def __init__(self, msg, error):
        Exception.__init__(self, message)
        self.error = error

class SizeException(PypoException):
    def __init__(self, msg, error):
        PypoException.__init__(self, msg, error)

class NotExistException(PypoException):
    def __init__(self, msg, error, path):
        PypoException.__init__(self, msg, error)
        self.path = path

class OperationAbordException(PypoException):
    def __init__(self, msg, error, cp, rp):
        PypoException.__init__(self, msg, error)
        self.cp = cp
        self.rp = rp

