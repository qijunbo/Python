#!/usr/bin/python
#Filename zipfolder.py
# Author:  Qi Junbo
# Created: September 28, 2018

import os,  time, sys

usage = "Usage: \n\t%s <SOURCE> <DEST> \
    \nExample: \n\t./zipfolder.py  /my/dir  /home/backup/dm-backup -v \
    \nParams:\n\tSOURCE: the folder you want to backup. \
    \n\tDEST: the folder which used to store backup archives. "

def zipFolderInto(source, destination ):
    timestr = time.strftime('%Y-%m-%d_%H%M%S',time.localtime(time.time()))
    day = time.strftime('%Y-%m-%d',time.localtime(time.time()))
    if not os.path.exists(source) :
        print "Can not find source folder %s ." % source
        return

    if not os.path.isdir(source):
        print "%s is not a folder." % source
        return

    if not os.path.exists(destination) :
        print "Can not find destination folder %s ." % source
        return

    if not os.path.isdir(destination):
        print "%s is not a folder." % destination
        return
    destination = os.path.join(destination,day)
    os.system("mkdir -p %s"  % destination)
    os.chdir(source)
    for filename in os.listdir(source):
        filepath = os.path.join(source,filename)
        if os.path.isdir(filepath):
            destfile = os.path.join(destination, ''.join([filename, "-", timestr, ".zip"]))
            print "zipping folder %s to %s" % (filepath, destfile)
            os.system("zip -rq  %s  %s"  % (destfile, filename))
        else:
            print "File %s ignored." % filepath
    return


argLen = len(sys.argv)

if argLen < 3 :
    print usage % sys.argv[0]
else:
    zipFolderInto(sys.argv[1],sys.argv[2])
