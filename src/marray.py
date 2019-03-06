from ovf import OvfFile
from fmrmodes import FMRModes
from fmrspectrum import FMRSpectrum
import numpy as np
import random
import copy


class Marray(FMRSpectrum, FMRModes):
    def __init__(self, path=None, parms=None, data=None, axis=None):
        # super().__init__()
        self.name=str(random.randint(0,10))
        self._path = path
        self._parms = parms
        
        if data is None:
            self._data = OvfFile(path, parms)
        else:
            self._data = copy.copy(data)
            self._data._array = self._data._array[:, :, :, :, axis]

    def save(self):
        self._data.save()

    @property
    def check_component(self):
        if self._data._array.shape[-1] is 1:
            return True

    def x(self, copy=False):
        if self.check_component is True:
            return(self)
        else:
            if copy is False:
                self._data._array = self._data._array[:, :, :, :, 2]
                return(self)
            else:
                return Marray(data=self._data, axis=2, path=self._path, parms=self._parms)

    def y(self, copy=False):
        if self.check_component is True:
                return(self)
        else:
            if copy is False:
                self._data._array = self._data._array[:, :, :, :, 1]
                return(self)
            else:
                print("As")
                return Marray(data=self._data, axis=1, path=self._path, parms=self._parms)
                

    def z(self, copy=False):
        if copy is False:
            self._data._array = self._data._array[:, :, :, :, 0]
            return(self)
        else:
            return Marray(data=self._data, axis = 0, path=self._path, parms=self._parms)