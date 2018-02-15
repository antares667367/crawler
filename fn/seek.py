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

    def seek_bins(self):
        """
        look for dissidents komrads
        recursively scans directories to extract files according to parameters
        :param extensions:
        :param path:
        :return:
        """
        s_pattern = "*"
        if "Linux" or "darwin" in self.system:
            s_root_path = "/"
        elif "win32" or "win64" in self.system:
            s_root_path = "C:"

        self.debug.log(s_root_path, "data path", self.info.line())
        self.debug.log(self.system, "system", self.info.line())
        self.debug.log(self.bin, "bin", self.info.line())

        for R, D, files in os.walk(s_root_path):
            for s_f in fnmatch.filter(files, s_pattern):
                if os.path.isfile(os.path.join(s_f)):
                    try:
                        if self.bin in magic.from_file(s_f):
                            self.debug.log(os.path.join(s_f),
                                           "{}".format(magic.from_file(os.path.join(s_f))),
                                           self.info.line())
                    except Exception as e:
                        print("{}".format(e.args))
                        pass
            else:
                pass