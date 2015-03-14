#!/usr/bin/env python2
import sys
from config import config as Config
from screensaver import xscreensaver

def main():
    config = Config(sys.argv[1:])
    ss = xscreensaver(config.lock_command, config.unlock_command)
    getattr(ss, config.mode)()
    exit()

if __name__ == "__main__":
    main()
