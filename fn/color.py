class Colors:
    """
    at2018
    color output class, provides escape codes for coloring
    """

    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    END = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    ALL = [HEADER,
           OKBLUE,
           OKGREEN,
           WARNING,
           FAIL,
           BOLD,
           UNDERLINE,
           END]

    @staticmethod
    def help():
        return "This is the help method for Color class.\n This class provides a way to color logs , ex Colors.WARNING will be red"
