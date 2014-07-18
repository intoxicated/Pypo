"""
    photo utility module
"""

import sys, os
import exifread as er


class PypoUtil:
    def __init__(self):
        pass

    @classmethod
    def getPath(self, filename):
        path = ''
        try:
            os.path.dirname(filename)
        except Exception as e:
            raise NotFoundException("File '%s' not found" % filename,\
                    e, path)

        return path
             
    @classmethod
    def changeWorkingDirectory(self, path):
        try:
            os.chdir(path)
        except Exception as e:
            raise NotFoundException("Path '%s' not found" % path, e, path)

    @classmethod
    def getfFiles(self, dirname):
        try:
            filelst = os.listdir(dirname)
        except Exception as e:
            raise NotFoundException("Directory %s is not found"\
                    % dirname, e, dirname)
        return filelst

    @classmethod
    def createDirectory(self, name, dirname):
        wd = os.getcwd()
        dpath = os.path.dirname(wd+dirname)
        if os.path.exists(dpath):
            raise OperationAboatException("Directory exists", Exception,\
                    "Create Directory")
        #create directory

    @classmethod
    def moveFilesTo(self, destination, filelst):
        pass

    @classmethod
    def getMetaInfo(self, filename):
        pass

      
