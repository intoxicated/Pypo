"""
    photo utility module
"""

import sys, os
import shutil
import exifread as er
import geopy as geo

from core.photo_exception import *

class PypoUtil:
    """ collection of useful methods in order to 
        organize photos
    """

    @classmethod
    def getPath(self, filename):
        """
            Get path of given file
            Working directory should be the directory that 
            contains file

            @param file name 
            @return full absolute path of the file
        """
        path = ''
        try:
            os.path.abspath(filename)
        except Exception as e:
            raise NotFoundException("File '%s' not found" % filename,\
                    e, path)

        return path
             
    @classmethod
    def changeWorkingDirectory(self, path):
        """
            Change working directory to given path 
            
            @param path of a directory
        """
        try:
            os.chdir(path)
        except Exception as e:
            raise NotFoundException("Path '%s' not found" % path, e, path)

    @classmethod
    def getFiles(self, dirname):
        """
            Get list of files in a directory

            @param path of a directory
            @return list of files in the directory
        """
        try:
            filelst = os.listdir(dirname)
        except Exception as e:
            raise NotFoundException("Directory '%s' is not found"\
                    % dirname, e, dirname)
        return filelst

    @classmethod
    def createDirectory(self, destpath, dirname):
        """
            Create a directory at a given path

            @param destpath desire path that directory to be created
            @param dirname directory name 

        """
        dpath = os.path.dirname(destpath+dirname)
        if os.path.exists(dpath):
            raise OperationAboatException("Directory exists", Exception,\
                    "Create Directory")
        #create directory
        os.mkdir(dpath)
        
    @classmethod
    def moveFilesTo(self, destination, filelst):
        """ 
            Move list of file to a destination. If duplicate name
            exists in the destination, it will be replaced based on
            permission

            @param destination path to a location
            @param filelst list of file paths

        """
        #if destination is not absolute, change it
        if not os.path.exists(destination):
            raise NotFoundExpcetion("Destination '%s' not exist" % dest,\
                    Exception, "Move file to")

        for each in filelst:
            try:
                shutil.move(each, destination)
            except IOError as e:
                raise OperationAbortException("No such file %s" % each,\
                        e, "Move file to loop")
            
    @classmethod
    def getMetaInfo(self, filename):
        """
            Get metadata of a file (assume its photo file)
            by using exifread module

            @param filename path of a file 
            @return photo object contains useful information 
        """
        #'Image Model'
        #'Image Orientation'
        #'GPS GPSLatitude'
        #'GPS GPSLongitude'
        #'Image DateTime'
        
        #check if file is exist, otherwise raise exception

        #open file 
        fd = open(filename, 'rb')
        tags = exifread.process_file(fd)

        #get file size
        fsize = os.stat(filename).st_size * 10 ** -6

        #get taken date
        pdate = tags['Image DateTime']
        pdevice = tags['Image Model']
        
        #default location value
        lng = None, lat = None

        #curret directory location
        ploc = os.path.dirname(filename)
        
        #check if location information is available
        if 'GPS GPSLatitude' is in tags.keys():
            lng = tags['GPS GPSLongitude']
            lat = tags['GPS GPSLatitude']

        #properly close file
        fd.close()

        return Photo(size=fsize, taken_date=pdate, taken_device=pdevice,
                location=(lng, lat), dirloc=ploc)


    @classmethod
    def getCityBy(self, longitude="", latitude=""):
        """
            Given a longitude and latitude, return 
            a city name 

            @param longitude,latitude floating number
            @return city name if they are valid
        """
        return ""
