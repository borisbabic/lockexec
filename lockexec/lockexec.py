#!/usr/bin/env python2
import sys
from config import config as Config
from screensaver import gnome
from screensaver import xscreensaver

def main():
    print "test"
    exit()
    config = Config(sys.argv[1:])
    if (config.xscreensaver):
        ssclass = xscreensaver
    elif(config.gnome):
        ssclass = gnome
    else:
        ssclass = globals()[config.screensaver]
    ss = ssclass(config.lock_command, config.unlock_command)
    if(config.daemon):
        ss.daemon()
    elif(config.smart):
        ss.smart()
    else:
        getattr(ss, config.mode)()
    exit()

if __name__ == "__main__":
    main()
