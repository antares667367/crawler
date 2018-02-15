import getopt, sys
import os
import fnmatch
import magic

from .database import Database  # db
from .seek import Scanner  # scanner
from .info import Info  # info
from .debug import Debug  # debug
from .color import Colors as F
from .bin import Bin


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
        self.daten = Scanner().os_probing()  # probe os
        self.system = self.daten["system"]
        self.bin = self.daten["bin_type"]

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

        if "Linux" or "LINUX" or "Unix" or "UNIX" or "darwin" in self.system:
            self.root_scan = "/"
        elif "win32" or "win64" in self.system:  # todo check real name in test
            self.root_scan = "C:"

    def inspect(self, db):
        """
        search the osfor bins(bin files)
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
                            BIN = Bin(db, bin, os.path.join(__root, bin))
                            print(BIN.show())
                            # BIN.aufzeichnung()
                            # self.debuggen.log(
                            #     "{}{}{}".format(F.OKGREEN, os.path.join(__root, "{} {}".format(bin, BIN.cve)), F.END),
                            #     OK, self.info.line())
                    except Exception as e:
                        self.debug.log("{}{} {}{}".format(F.FAIL, e.args, bin, F.END), ERR, self.info.line())
                    else:
                        pass

    def usage(self):
        """
        display Moscow's instructions
        """
        # directives from Moscow
        print("Usage: ./checksysvce "
              "-u (--updatedatabase) [-f database_filepath] | "
              "-c (--checkvuln) [-f binary_filepath] | "
              "-q (--quiery) [-f binary_filepath] | "
              "-Q (--quit) | "
              "-h (--help) | "
              "-l (--listvuln) [-f binary_pathfile]")

    def parse_options(self):
        """
        parse options from checksysvce
        """
        if "-u" in self.actual:

            db_path = os.path.dirname(self.db_path)  # strip given path (-f) to assess the path
            db_name = os.path.splitext(self.db_path)[0]  # and the filename (without extension)
            db = Database(db_path, "{}.db".format(db_name))  # the sys to be searched
            db.insert_ko("os",
                         self.daten)  # insert os fingerprint in db
            self.inspect(db)  # inspect sys for bins
        elif "-c" in self.actual:
            print("NA")
        elif "-q" in self.actual:
            print("NA")
        elif "-l" in self.actual:
            print("NA")

    def menu(self):
        """
        listen to Moscow's orders and direct actions
        """
        try:
            opts, args = getopt.getopt(self.args, "hulcf:q:Q")
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
