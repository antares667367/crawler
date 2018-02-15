import inspect


class Info:
    """
    at2018
    provides line number when line is called
    """

    def __init__(self, enabled=True):
        self.enabled = enabled

    @staticmethod
    def line():
        callerframerecord = inspect.stack()[1]
        frame = callerframerecord[0]
        info = inspect.getframeinfo(frame)
        return info.lineno
