import os

from tinydb import TinyDB, where

from .debug import Debug
from .info import Info


class Database:
    def __init__(self, path, name):
        """
        Inits a new tinyDB
        :param path:
        :param name:
        """
        self.info = Info(enabled=True)  # set info -(line number for debug)
        self.debug = Debug(internal_debug=True, color_output=True)  # set debug class
        self.debug.setLogger("database.py")  # set logger with file name
        self.db_path = os.path.join(path, name)
        try:
            self.database = TinyDB(os.path.join(path, name))
        except Exception as e:
            print(e.args)
            pass
        else:
            pass

    def insert(self, key, version, _hash, cve, state):
        """
        Inserts in tinyDB
        :param key:
        :param version:
        :param _hash:
        :param cve:
        :return:
        """
        try:
            self.database.insert({'name': key, 'version': version, 'hash': _hash, 'cve': cve, 'state': state})
        except Exception as e:
            print(e.args)
            pass
        else:
            pass

    def insert_ko(self, k, o):
        # insert object with key:obj pattern
        try:
            self.database.insert({k: o})
        except Exception as e:
            print(e.args)
            pass
        else:
            pass

    def update(self, key, version, _hash, cve):
        """
        Updates in tinyDB
        :param key:
        :param version:
        :param _hash:
        :param cve:
        :return:
        """
        try:
            self.database.update({'name': key, 'version': version, 'hash': _hash, 'cve': cve})
        except Exception as e:
            print(e.args)
            pass
        else:
            pass

    def display(self):
        """
        Display in tinyDB
        :return:
        """
        try:
            l = len(self.database)
            self.debug.log("items in {} {}".format(self.db_path, l), "database.py", self.info.line())
            for item in self.database:
                self.debug.log("{}".format(item), "item", self.info.line())
        except Exception as e:
            print(e.args)
            pass
        else:
            pass

    def _search(self, attrib: str, attrib_val: str):
        """
        Search in tinyDB
        :return: results
        """
        try:
            return self.database.search(where(attrib) == attrib_val)
        except Exception as e:
            print(e.args)
            pass
