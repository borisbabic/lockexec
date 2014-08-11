========
LockExec
=======
LockExec lets you do stuff on screen lock, or screen unlock.
Currently supported screensaver: xscreensaver.

Installation:
pip install https://github.com/borisbabic/lockexec/archive/master.zip

There are two modes, daemon and once.
Daemon launches the script and then waits for an indefinite number of lock/unlock signals
Once executes the lock command, locks the screen, and does unlock command when the screen is unlocked

example::
    lockexec --daemon --lock-command "echo hello" --unlock-command "echo world"
