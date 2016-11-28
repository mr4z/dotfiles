#!/usr/bin/env python
import i3ipc
import time
import i3
import subprocess
fullscreen = i3ipc.Connection().get_tree().find_fullscreen()
if fullscreen == []:
    i3.exec('xautolock -locknow')
