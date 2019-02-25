#!/usr/bin/python
#Filename createIndex.py
# Author:  Qi Junbo
# Created: February 22, 2019
import os,  datetime, sys
from __builtin__ import file
 
def createIndexFor(_dir):
    """
    create index.html page for files in _dir.
        
    """
    index = "index.html"
    
    cwd = os.getcwd()
    if not _dir.startswith( '/' ) :
        _dir =  os.path.join(cwd , _dir)
        print _dir
 
    if not os.path.exists(_dir) :
        print "Can not find folder [%s] " % _dir
        return
    
    for filename in os.listdir(_dir):
        os.system("echo '' >%s/%s" %( _dir, index))
        filepath = os.path.join(_dir,filename)
        if os.path.isdir(filepath): # ignore folders, links.
            os.system("echo '<a href=\"%s/index.html\">%s</a>' >>%s/%s" %(filename, filename, _dir, index))
            createIndexFor(filepath)
        elif os.path.isfile(filepath) :
            os.system("echo '<img src=\"%s\"><br/>' >>%s/%s" %(filename, _dir, index))
    return


 
    

usage = "Generate index.html for specified dir. \nUsage: \n\t%s <PATH>" 
    
def main():
    argLen = len(sys.argv)
    if argLen <= 1:
        print usage %(sys.argv[0])
        return
    createIndexFor(sys.argv[1])
    return

if __name__ == '__main__':
    main()
    exit()
        
