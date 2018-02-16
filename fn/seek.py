import fnmatch
import platform
import magic
import sys

from .info import Info
from .debug import Debug
import os
from pathlib import Path


class Scanner:
    """
    gather os info && scan dir accordingly
    TODO make cross platform
    at2018
    """

    def __init__(self):
        """
        init class with pseudo OS fingerprint
        """
        # setting debug and info for class
        self.debug = Debug(internal_debug=True)
        self.info = Info(enabled=True)
        self.debug.setLogger(os.path.basename(__file__))
        self.system = ""
        self.arch = ""
        self.bin = ""

    def os_probing(self):
        """
        assess town situation
        perform pseudo fingerprint using builtin platform library
        :return: platform.platform
        """
        # osi stands for OS info
        stadt = platform
        # update self.plateform
        self.system = stadt.system()
        self.arch = stadt.architecture()[0]
        self.bin = stadt.architecture()[1]
        return {"system": stadt.system(), "platform": stadt.platform(), "sys_version": stadt._sys_version(),
                "processor": stadt.processor(),
                "w32_version ": stadt.win32_ver(), "mac_version": stadt.mac_ver(), "arch": stadt.architecture(),"bin_type":stadt.architecture()[1]}
