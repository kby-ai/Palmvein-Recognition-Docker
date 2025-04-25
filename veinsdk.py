import os

from ctypes import *

libPath = os.path.abspath(os.path.dirname(__file__)) + '/libvein.so'
veinsdk = cdll.LoadLibrary(libPath)

getMachineCode = veinsdk.getMachineCode
getMachineCode.argtypes = []
getMachineCode.restype = c_char_p

setActivation = veinsdk.setActivation
setActivation.argtypes = [c_char_p]
setActivation.restype = c_int32

initSDK = veinsdk.initSDK
initSDK.argtypes = []
initSDK.restype = c_int32

getFeature = veinsdk.get_feature
getFeature.argtypes = [c_char_p, c_ulong, POINTER(c_float)]
getFeature.restype = c_int32

getScore = veinsdk.get_score
getScore.argtypes = [POINTER(c_float), c_ulong, POINTER(c_float), c_ulong]
getScore.restype = c_float