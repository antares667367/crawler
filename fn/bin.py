import hashlib
from .check_cve import Cve
from .debug import Debug
from .info import Info


class Bin:
    """
    represents a binary
    """

    def __init__(self, database, name, path, version=None):
        """
        init object
        """
        self.name = name
        self.path = path
        self.hash = self.hash(self.path)
        self.version = version
        self.database = database
        self.info = Info(enabled=True)  # set info -(line number for debug)
        self.debug = Debug(internal_debug=True, color_output=True)  # set debug class
        self.debug.setLogger("bin.py")  # set logger with file name
        self.cve = Cve().search(name, version)
        self.summary = {"bin_name": self.name, "bin_path": self.path,
                        "state": "found" if self.cve else "not found"}

    def __del__(self):
        self.debug.log("{} removed from ram".format(self.name), "bin.py", self.info.line())

    def rec_in_db(self):
        """
        the bin infos are recorded in db
        :return:
        """
        self.database.insert(
            self.path,
            self.version, self.hash,
            self.cve,"found" if self.cve else "not found")  # record in db

    def hash(self, path):
        """
        produce hash > sha256
        :param path:
        :return:
        """
        h = hashlib.sha256()
        with open(path, 'rb', buffering=0) as f:
            for b in iter(lambda: f.read(128 * 1024), b''):
                h.update(b)
            return h.hexdigest()

    def show(self):
        return {"name": self.name, "path": self.path, "hash": self.hash, "version": self.version, "cve": self.cve,
                "summary": self.summary}
