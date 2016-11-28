#!/usr/bin/env python
import i3
import time

term = 'urxvtc'

def ws_term():
    i3.exec(term)
    i3.split('h')
    time.sleep(1.0)
    i3.exec(term)
    i3.split('h')
    time.sleep(0.1)
    i3.focus('left')
    i3.split('vertical')
    i3.exec(term)
    time.sleep(0.1)
    i3.focus('right')
    i3.split('vertical')
    i3.exec(term +' -e htop')
def run():
    i3.workspace('1:term')
    i3.layout('default')
    ws_term()
    i3.workspace('2:web')

if __name__ == '__main__':
    run()
