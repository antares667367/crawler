import fnmatch
import getopt
import os
import sys

import magic

from .bin import Bin
from .color import Colors as F
from .database import Database  # db
from .debug import Debug  # debug
from .info import Info  # info
from .seek import Scanner  # scanner
from .check_cve import Cve


class Main:
    def __init__(self, args):
        """
        Constructor of the fn object
        """
        self.actual = ""  # set the param chosen for the menu
        self.root_scan = ""  # set the root scan
        self.db_path = ""  # set the path where the databases will be stored
        self.info = Info(enabled=True)  # set info -(line number for debug)
        self.debug = Debug(internal_debug=True, color_output=True)  # set debug class
        self.debug.setLogger("main.py")  # set logger with file name
        self.args = args  # get args from main script
        self.osfp = Scanner().os_probing()  # probe os
        self.system = self.osfp["system"]
        self.bin = self.osfp["bin_type"]

    def out(self):
        """
        exit the script
        :return:
        """
        sys.exit()

    def get_sys_root(self):
        """
        determine system root , according to OS
        :return:
        """

        if "Linux" or "Unix" or "darwin" in self.system:
            self.root_scan = "/"
        elif "win32" or "win64" in self.system:
            self.root_scan = "C:"

    def inspect(self, db):
        """
        search the os for bin files
        :return:
        """
        db = db  # get db
        OK = "{}{}{}".format(F.OKGREEN, "OK", F.END)
        ERR = "{}{}{}".format(F.FAIL, "ERR", F.END)
        self.get_sys_root()  # assess search_path
        self.debug.log(self.root_scan, "inspekt()", self.info.line())
        for __root, dirs, bins in os.walk(self.root_scan):  # loop root_scan
            for bin in fnmatch.filter(bins, "**"):  # get bins corresponding with the pattern
                #
                if os.path.isfile(os.path.join(__root, bin)) and not os.path.islink(os.path.join(__root, bin)):
                    try:
                        if self.bin in magic.from_file(os.path.join(__root, bin)):
                            BIN = Bin(db, bin, os.path.join(__root, bin))  # create object
                            self.debug.log(BIN.show(), "inspect()", self.info.line())  # display for debug
                            BIN.rec_in_db()  # the object records itself in db
                            del BIN  # once done, the object deletes itseflf to free up ram
                    except Exception as e:  # raise error if any
                        self.debug.log("{}{} {}{}".format(F.FAIL, e, bin, F.END), ERR, self.info.line())
                    else:
                        pass

    def usage(self):
        """
        display optins
        """
        # directives from Moscow
        print("Usage: ./checksysvce \n"
              "p3sbc Python3 simple bin crawler (finds bin over the system and get corresponding CVEs) "
              "-u (--updatedatabase) [-f database_filepath] | # pop database\n"
              "-c (--checkvuln) [-f database_filepath] | # list found\n"
              "-q (--query) [-f database_filepath] | # query by attribute\n"
              "-Q (--quit) | # exit the script\n"
              "-h (--help) | # display this\n"
              "-l (--listvuln) [-f binary_pathfile] | # list all\n"
              "-s (--single) | # EXPERIMENTAL / use API for single bin (no hash or path ,"
              " as the bin can be on the system or not.Only CVEs are displayed if any)\n")

    def parse_options(self):
        """
        parse options from checksysvce
        """

        db_path = os.path.dirname(self.db_path)  # strip given path (-f) to assess the path
        db_name = os.path.splitext(self.db_path)[0]  # and the filename (without extension)
        db = Database(db_path, "{}.db".format(db_name))  # the sys to be searched
        if "-u" in self.actual:
            db.insert_ko("os",
                         self.osfp)  # insert os fingerprint in db
            self.inspect(db)  # inspect sys for bins
        elif "-l" in self.actual:
            db.display()
        elif "-c" in self.actual:
            for sta in db._search('state', 'found'):
                self.debug.log(sta, "database.py", self.info.line())
        elif "-c" in self.actual:
            for sta in db._search('state', 'found'):
                self.debug.log(sta, "database.py", self.info.line())
        elif "-q" in self.actual:
            att = input("attribute [name,hash,state] ex: name \n > ")
            val = input("attribute value ex: found \n > ")
            for sta in db._search(str(att), str(val)):
                self.debug.log(sta, "database.py", self.info.line())
        elif "-s" in self.actual:
            bin = input("binary name \n > ")
            version = input("binary version (if any , othrwise type None)\n > ")
            cve = Cve().search(bin, version)
            self.debug.log({"name": bin, "version": version, "cve": cve, "state": "found" if cve else "not found"})

    def menu(self):
        """
        listen to Moscow's orders and direct actions
        """
        try:
            opts, args = getopt.getopt(self.args, "hulcf:qQs")
        except getopt.GetoptError as err:
            # print help information and exit:
            print(err)  # will print something like "option -a not recognized"
            self.usage()
            self.out()
        for o, a in opts:
            if o in ("-u", "--updatedatabase"):
                self.actual = o
            elif o in ("-h", "--help"):
                self.usage()
                self.out()
            elif o in ("-c", "--checkvuln"):
                self.actual = o
            elif o in ("-l", "--listvuln"):
                self.actual = o
            elif o in ("-q", "--query"):
                self.actual = o
            elif o in ("-s", "--single"):
                self.actual = o
            elif o in "-f":
                if a is not None:
                    self.db_path = a
                else:
                    print("-f must be followed by a valid filepath")
                    self.usage()
                    self.out()
            elif o in ("-Q", "--quit"):
                self.out()
            else:
                print("unhandled option")
                self.usage()
                self.out()

        self.parse_options()
