#!usr/bin/env python

#import statements
from datetime import datetime
import urllib
from urllib import request
import ctypes  # An included library with Python install.

def main():
    while(True):
        now = datetime.now().time().isoformat().split(':')
        if int(now[1]) % 5 == 0:
            cs3205()
            cs2330()
            econ2020()


def econ2020():
    class_file = urllib.reequest.urlopen("view-source:https://rabi.phys.virginia.edu/mySIS/CS2/page.php?Semester=1158&Type=Group&Group=Economics")
    for line in class_file:
        if 'ECON2020' in str(line) and 'Lecture' in str(line) and 'Open' in str(line)

def cs3205():
    class_file = urllib.request.urlopen("https://rabi.phys.virginia.edu/mySIS/CS2/page.php?Semester=1158&Type=Group&Group=CompSci")
    for line in class_file:
        if 'CS3205' in str(line) and 'Open' in str(line):
            ctypes.windll.user32.MessageBoxA(0, "O", "CS3205",1)


def cs2330():
    class_file = urllib.request.urlopen("https://rabi.phys.virginia.edu/mySIS/CS2/page.php?Semester=1158&Type=Group&Group=CompSci")
    counter = 0
    for line in class_file:
        if 'CS2330' in str(line) and 'Enrollment Requirements: Undergraduate Engineering' not in str(line):
            counter += 1
            if counter > 4:
                ctypes.windll.user32.MessageBoxA(0, "R", "CS2330",1)

if __name__=='__main__':
    main()
