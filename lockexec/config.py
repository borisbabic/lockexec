import json
import os
import argparse

class baseConfig(object):
    @property
    def config_file(self):
        return self._config_file

    @config_file.setter
    def config_file(self,value):
        if (value):
            self._config_file = value

    def updateAttributes(self,data):
        for key in data:
            setattr(self,key,data[key])

    def parseFile(self):
        f = None
        try:
            f = open(self.config_file,'r')
            try:
                data=json.load(f)
                self.updateAttributes(data)
            except ValueError:
                if os.path.isfile(self.config_file) > 0:
                    print "Bad Config File"
        except IOError:
            if os.path.isfile(self.config_file):
                print "Couldn't open config file {file}".format(file = self.config_file)
        finally:
            if f:
                f.close()

    def parseOptions(self):
        data_list = [{key :getattr(self.options,key)} for key in dir(self.options) if key[0] != '_']
        data = reduce(lambda x,y : dict(x.items() + y.items()) , data_list)
        self.updateAttributes(data)

class config(baseConfig):
    def __init__(self,argv):
        self.log_file = os.path.expanduser('~/.lockexec.log')
        self._config_file = os.path.expanduser('~/.lockexec')
        self.lock_command = "echo lock"
        self.unlock_command = "echo unlock"
        self.screensaver = "xscreensaver"
        self.mode = "smart"
        self.parseFile()
        self.parserInit(argv)
        self.config_file=self.options.config_file
        self.parseFile()
        self.parseOptions()

    def parserInit(self, argv):
        parser = argparse.ArgumentParser(description = "Python app for doing stuff on lock/unlock")
        parser.add_argument('-l', '--lock-command', action = 'store', help = 'Lock Command (default = "{default}")'.format(default = self.lock_command), default = self.lock_command)
        parser.add_argument('-u', '--unlock-command', action = 'store', help = 'Unlock Command (default = "{default}")'.format(default = self.unlock_command), default = self.unlock_command)
        parser.add_argument('-c', '--config-file', action = 'store', help = 'Config file to use (default = {default})'.format(default = self.config_file), default = self.config_file)
        parser.add_argument('--log-file', action = 'store', help = 'Log file to use (NOT IMPLEMENTED')#(default = {default})'.format(default = self.log_file), default = self.log_file)
        temp = parser.add_argument_group('Choose one (default = {default})'.format(default = self.mode))
        ssgroup = temp.add_mutually_exclusive_group()
        ssgroup.add_argument('-s', '--smart', action = "store_true", help = "Executes LOCK_COMMAND, locks, and executes UNLOCK_COMMAND on unlock", default = False)
        ssgroup.add_argument('-d', '--daemon', action = "store_true", help = "Execute UNLOCK_COMMAND, LOCK_COMMAND on unlock/lock", default = False)
        temp2 = parser.add_argument_group('Choose a locker (default = {default})'.format(default = self.screensaver))
        lockerGroup = temp2.add_mutually_exclusive_group()
        lockerGroup.add_argument('--gnome', action = "store_true", help = "Use gnome-screensaver", default = False)
        lockerGroup.add_argument('--xscreensaver', action = "store_true", help = "Use xscreensaver", default = False)
        self.options = parser.parse_args(argv)


