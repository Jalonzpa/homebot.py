#!/usr/bin/python
import os
import sys
import time

def sprint(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
	time.sleep(0.03)


sprint("Yeet")
sprint("Yote")
