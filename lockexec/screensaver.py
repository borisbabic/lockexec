from time import sleep
import subprocess
import shlex
class screensaver(object):
    """Parent class for screensavers"""

    LOCK = "LOCK"
    UNLOCK = "UNLOCK"

    def __init__(self, lock_command, unlock_command):
        self.once = False
        self.lock_command = lock_command
        self.unlock_command = unlock_command
        assert (self.LOCKER)
        assert (self.CHECKER)

    def run(self, command, hide = True, **kwargs):
        if(hide):
            temp= {'stdout' : subprocess.PIPE, 'stderr' : subprocess.PIPE}
            kwargs.update(temp)
        #if(' ' in command):
            #command = shlex.split(command)
        return subprocess.Popen(command, shell=True, **kwargs)

    def unlockCommand(self, hide=False):
        return self.run(self.unlock_command)

    def lockCommand(self, hide=False):
        return self.run(self.lock_command)

    def lock(self):
        return self.run(self.LOCKER)

    def smart(self):
        self.lockCommand()
        self.lock()
        self.once = True
        self.daemon()
        exit()

    def compare(self, temp):
        if (self.LOCK_STR in temp):
            return self.LOCK
        elif(self.UNLOCK_STR in temp):
            return self.UNLOCK
        else:
            return None

    def getLine(self):
        return self.proc.stdout.readline().__str__()

    def check(self):
        """
        GETS the status returns LOCK/UNLOCK for locked/unlocked
        or the result of self.compare().
        """

    def daemonWhile(self):
        while True:
            temp = self.check()
            if (self.latest != temp and temp != None ):
                if (temp == self.UNLOCK):
                    self.unlockCommand()
                    if (self.once):
                        return
                elif (temp == self.LOCK):
                    self.lockCommand()
                self.latest = temp
            sleep(1)

    def daemon(self):
        raise NotImplementedError('No Daemon Found')


class gnome(screensaver):

    LOCKER = "gnome-screensaver-command -l"
    CHECKER = "gnome-screensaver-command -q"
    LOCK_STR = "is active"
    UNLOCK_STR = "is inactive"

    def check(self):
        self.proc = self.run(self.CHECKER)
        return self.compare(self.getLine())

    def daemon(self):
        self.latest = self.check()
        self.daemonWhile()


class xscreensaver(screensaver):

    LOCKER = "xscreensaver-command -lock"
    CHECKER = "xscreensaver-command -watch"
    LOCK_STR = "LOCK"
    UNLOCK_STR = "UNBLANK"

    def watcher(self):
        self.proc = self.run(self.CHECKER)

    def check(self):
        return self.compare(self.getLine())

    def daemon(self):
        self.watcher()
        self.latest = self.check()
        self.daemonWhile()

