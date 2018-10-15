#!/usr/bin/python
#Filename deloldfile.py
# Author:  Qi Junbo
# Created: September 28, 2018
import os,  datetime, sys
 
def delFileOlderThan(_dir, _days, _filetype, recursive = False, verbose = False):
    """
    remove the files of type <_filetype> in folder <_dir> old than <_days> days.
        
    """
    if _filetype is None or _filetype in ('-v', '-r'):
        _filetype = ''    
    
    today = (datetime.datetime.now()-datetime.datetime(1970,1,1)).total_seconds()
    if not os.path.exists(_dir) :
        print "Can not find %s ." % _dir
        return
    for filename in os.listdir(_dir):
        filepath = os.path.join(_dir,filename)
        if meetConditions(filepath, _days, _filetype):
            os.system("rm -f %s" %filepath)
            if verbose :
                print "Removing file [%s] created %s days ago." %(filepath, str(dif))
        elif os.path.isdir(filepath) and recursive :
            delFileOlderThan(filepath, _days, _filetype, recursive, verbose )
    return

def meetConditions(file, days, filetype):
    if not os.path.isfile(file): # ignore folders, links.
        return False
    if not file.endswith(filetype): # ignore the files which suffix doesn't meet.
        return False
    file_date = os.path.getmtime(filepath)
    dif = int((today -  file_date ) / 86400) #  1 day == 86400 seconds
    if dif > _days :
        return True
    else:
        return False
    

usage = "Usage: \n\t%s <PATH> <days> <fileType> [-r|-v] \
    \nExample: \n\t./deloldfile.py  /my/dir  30 -v \
    \nParams:\n\tPATH: in which you want to remove files. \n\tdays: old than given days.\
    \nOptions:\n\t-r recursively. \n\t-v verbosely."            

if __name__ == '__main__':
    argLen = len(sys.argv)
    if argLen < 3:
        print usage %(sys.argv[0])
    elif argLen < 4: 
        delFileOlderThan(sys.argv[1], int(sys.argv[2]))
    elif argLen <5:
        delFileOlderThan(sys.argv[1], int(sys.argv[2]), sys.argv[3])
    else:
        recursively = False
        verbosely = False
        if "-r" in sys.argv :
            recursively = True
        elif "-v" in sys.argv :
            verbosely = True
        delFileOlderThan(sys.argv[1], int(sys.argv[2]), sys.argv[3], recursively,verbosely)