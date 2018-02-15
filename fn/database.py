import os
from tinydb import TinyDB, Query
from .info import Info
from .debug import Debug


class Database:
    def __init__(self, path, name):
        """
        Inits a new tinyDB
        :param path:
        :param name:
        """
        try:
            self.database = TinyDB(os.path.join(path, name))
        except Exception as e:
            print(e.args)
            pass
        else:
            pass

    def insert(self, key, version, _hash, cve):
        """
        Inserts in tinyDB
        :param key:
        :param version:
        :param _hash:
        :param cve:
        :return:
        """
        try:
            self.database.insert({'name': key, 'version': version, 'hash': _hash, 'cve': cve})
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
            for item in self.database:
                print(item)
        except Exception as e:
            print(e.args)
            pass
        else:
            pass

    def search(self, request):
        """
        Search in tinyDB
        :return: results
        """
        try:
            Q = Query()
            self.database.search(Q.name == request)
        except Exception as e:
            print(e.args)
            pass
        else:
            pass
