#!/usr/bin/env python
import i3
import time

def ws_dev():
    i3.workspace('3:dev')
    i3.exec('zathura ~/Books/Python/izuchaem-python.pdf')
    i3.focus('left')
    time.sleep(0.2)
    i3.exec('urxvtc -e vim ~/source/stud/task.py')

if __name__ == '__main__':
    ws_dev()
