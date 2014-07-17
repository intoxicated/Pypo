"""
    Photo reperesentation model

    property: size, dimension, taken_date, taken_device, 
              quality, location (if available)
"""

import datetime

class Photo(object):
    def __init__(self, **kwargs):
        self._size = kwargs['size']
        self._dimension = kwargs['dimension']
        self._taken_date = kwargs['taken_date']
        self._taken_device = kwargs['taken_device']
        self._quality = kwargs['quality']
        self._location = kwargs['location']
        self._dirloc = ''

    @property
    def location(self):
        return self._location

    @location.setter
    def location(self, lat, log):
        self._location = (lat, log)

    @property
    def dirloc(self):
        return self._dirloc

    @dirloc.setter
    def dirloc(self, dirloc):
        self._dirloc = dirloc

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, size):
        self._size = size

    @property
    def dimension(self):
        return self._dimension

    @dimension.setter
    def dimension(self, w, h):
        self._dimension = (w, h)

    @property
    def taken_date(self):
        return self._taken_date

    @taken_date.setter
    def taken_date(self, date):
        self.taken_date = date

    @property
    def quality(self):
        return self._quality

    @quality.setter
    def quality(self, qual):
        self._quality = qual


