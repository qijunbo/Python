#!/usr/bin/python
#Filename deloldfile.py
# Author:  Qi Junbo
# Created: September 28, 2018
import os,  datetime, sys
 
def delFileOlderThan(_dir, _days, recursive = False, verbose = False):
    today = (datetime.datetime.now()-datetime.datetime(1970,1,1)).total_seconds()
    if not os.path.exists(_dir) :
        print "Can not find %s ." % _dir
        return
    for filename in os.listdir(_dir):
        filepath = os.path.join(_dir,filename)
        #Judgment is a file
        if os.path.isfile(filepath):
            file_date = os.path.getmtime(filepath)
            dif = int((today -  file_date ) / 86400)
            if dif > _days :
                os.system("rm -f %s" %filepath)
                if verbose :
                    print "Removing file [%s] created %s days ago." %(filepath, str(dif))
        elif os.path.isdir(filepath) and recursive :
            delFileOlderThan(filepath, _days, recursive, verbose)

usage = "Usage: \n\t%s <PATH> <days> [-r|-v] \
    \nExample: \n\t./deloldfile.py  /my/dir  30 -v \
    \nParams:\n\tPATH: in which you want to remove files. \n\tdays: old than given days.\
    \nOptions:\n\t-r recursively. \n\t-v verbosely."            
argLen = len(sys.argv)

if argLen < 3 :
    print usage %(sys.argv[0])
elif argLen < 4  : 
    delFileOlderThan(sys.argv[1], int(sys.argv[2]))
else:
    recursively = False
    verbosely = False
    if "-r" in sys.argv :
        recursively = True
    elif "-v" in sys.argv :
        verbosely = True
    delFileOlderThan(sys.argv[1], int(sys.argv[2]), recursively,verbosely)