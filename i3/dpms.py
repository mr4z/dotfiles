#!/usr/bin/env python
import i3
import subprocess
import time

while True:
    time.sleep(10.0)
    pidof = subprocess.Popen(['pidof', 'i3lock'], stdout=subprocess.PIPE,
                                                  stderr=subprocess.PIPE)
    out, err = pidof.communicate()
    if out == b'':
        i3.exec('xset -dpms')
