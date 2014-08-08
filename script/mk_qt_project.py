#!/usr/bin/env python
# coding=utf-8
import sys,os
cppList = []
hList   = []
oList   = []

def SearchFile(path):
    arr = path.split('/')
    if not arr[-1].startswith('.'):
        if os.path.isdir(path):
            folderList = os.listdir(path)
            for x in folderList: 
                SearchFile(path+'/'+x)
        elif os.path.isfile(path):
            if -1 !=  path.rfind(".cpp"):
                cppList.append(path)
            elif -1 != path.rfind(".h"):
                hList.append(path)
            else:
                oList.append(path)

def FindFile(path):
    if not path:
        print "This is not path!\n"
        return
    else:
        SearchFile(path)

if __name__ == "__main__":
    paraL = len(sys.argv)
    if paraL < 2:
        print("invalid parameter\n")
    else:
        for f in sys.argv[1:paraL-1]:
            FindFile(f)

    try:
        fPro = open(sys.argv[paraL - 1], 'w')
    except IOError:
        print("open file: %s failure!\n"%sys.argv[paraL-1])
    else:    
        print("start making project file-----------------------! ")
        fPro.write("SOURCES += \\\n")
        for cpp in cppList:
            fPro.write(cpp+"\\\n")
            print("write file: %s"%cpp)                   
          
        fPro.write("\n\n")
        fPro.write("HEADERS += \\\n")
        for h in hList:
            fPro.write(h+"\\\n")
            print("write file: %s"%h)
    
        fPro.write("\n\n")
        fPro.write("OTHER_FILES += \\\n")
        for o in oList:
            fPro.write(o+"\\\n")
            print("write file: %s"%o)

        fPro.close()        
        print("Make sucessfully project file -------------------!") 
