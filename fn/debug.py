from .color import Colors


class Debug:
    """
    at2018
    debug class , if specified , color output will be true or false . default is True
    """

    def __init__(self, internal_debug, color_output=True, unittest=False):
        """
        
        init debug class
        :param internal_debug: bool
        :param color_output bool defaul to True
        :param unittest default set to False , used for unittest
        """
        self.logger = " - "
        self.internal_debug = internal_debug
        self.color_output = color_output
        self.unittest = unittest

    def setUnit(self, unittest):
        """
        setter for unittest
        :param unittest bool
        """
        self.unittest = unittest

    def setDebug(self, internal_debug):
        """
        setter for internal debug
        :param internal_debug: bool
        :return:
        """
        self.internal_debug = internal_debug

    def setLogger(self, value):
        self.logger = value

    def setOutput(self, color_output):
        """
        setter for color_output
        :param color_output:
        :return:
        """
        self.internal_debug = color_output

    def log(self, something, describe="::DEBUG", line=0):
        # line is set to 0 if not supplied

        """
        logs something, has a default value for describe if not set
        :param line: nls means no line supplied, line is supplied by hand of using class info
        :param something:
        :param describe:
        """
        if self.internal_debug:
            prepare = " ".join(
                [Colors.FAIL, self.logger, "[line", str(line), "] ", str(describe), Colors.OKGREEN, " >> ",
                 Colors.WARNING, str(something)]) if self.color_output else " ".join(
                [self.logger, "[line", str(line), "] ", str(describe), str(something)])
            if self.internal_debug:
                if self.unittest:
                    return prepare
                else:
                    print(prepare)
