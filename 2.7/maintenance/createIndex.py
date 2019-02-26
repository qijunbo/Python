#!/usr/bin/python
#Filename createIndex.py
# Author:  Qi Junbo
# Created: February 22, 2019
import os, io, datetime, sys
from __builtin__ import file

###io.open('textfile.txt', 'w', encoding='utf-8')

def writeTextToFile(text, file):
   with open(file,'wb') as f:
      f.write(text)
      f.close()

 
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
    text = '<html><head><meta http-equiv=\"Content-Type\" content=\"text/html; charset=GBK\" /></head>\n'
    for filename in os.listdir(_dir):
        filepath = os.path.join(_dir,filename)
        if os.path.isdir(filepath): # ignore folders, links.
            text = text + ( '<a href=\"%s/index.html\">%s</a><br/>\n' %(filename, filename))
            createIndexFor(filepath)
        elif os.path.isfile(filepath) and filepath.endswith('jpg') :
            text = text + ('<img src=\"%s\"><br/>\n' %(filename))
    text = text + '</html>'
    writeTextToFile(text, os.path.join( _dir, index))
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
        
