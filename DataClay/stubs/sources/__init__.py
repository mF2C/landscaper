# Automatically created by dataClay
import os
import sys

from dataclay import dclayMethod, dclayEmptyMethod, DataClayObject
from dataclay.contrib.dummy_pycompss import *

from logging import getLogger
getLogger('dataclay.deployed_classes').debug('Package path: ./demo/stubs/sources')
StorageObject = DataClayObject

###############################################################
######### <Class-based imports>:


######### </Class-based imports>
###############################################################

try:
    from pycompss.api.task import task
except ImportError:
    from dataclay.contrib.dummy_pycompss import *

