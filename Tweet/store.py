import sys


class Logger(object):
    def __init__(self, fileN="twitter_streaming.py"):
        self.terminal = sys.stdout
        self.log = open(fileN, "w")

    def write(self, message):
        self.terminal.write(message)
        self.log.write(message)

    def flush(self):
        pass


sys.stdout = Logger("target_file.txt")
