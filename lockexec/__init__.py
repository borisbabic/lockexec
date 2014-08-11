#!/usr/bin/env python2

import sys
import subprocess
import argparse
from screensaver import xscreensaver

DEFAULT_LOCK_COMMAND="echo lock"
DEFAULT_UNLOCK_COMMAND="echo unlock"

def parse_args(args):
    parser = argparse.ArgumentParser(description="Veni Vidi Vici")
    parser.add_argument('-l','--lock-command', action='store', help="Lock Command", default=DEFAULT_LOCK_COMMAND)
    parser.add_argument('-u','--unlock-command', action='store', help="Unlock Command", default=DEFAULT_UNLOCK_COMMAND)
    temp = parser.add_argument_group('Choose one')
    ssgroup = temp.add_mutually_exclusive_group(required=True)
    ssgroup.add_argument('-s','--smart', action="store_true", help="lockCommand, lock, and unlockCommand on unlock", default=False)
    ssgroup.add_argument('-d','--daemon', action="store_true", help="Launch a daemon that does unlockCommand,lockCommand on unlock/lock", default=False)
    options=parser.parse_args(args)
    return options

def main():
    options = parse_args(sys.argv[1:])
    screensaver = xscreensaver(options.lock_command, options.unlock_command)
    if(options.daemon):
        screensaver.daemon()
    elif(options.smart):
        screensaver.smart()
    exit()


if __name__ == "__main__":
    main()
