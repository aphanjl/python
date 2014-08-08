#!/usr/bin/env python
# coding=utf-8

import sys, os

def SearchFile(path,directoryList):
    arr = path.split('/')
    if not arr[-1].startswith('.'):
        if os.path.isdir(path):
            folderList = os.listdir(path)
            for x in folderList: 
                SearchFile(path+'/'+x, directoryList)
        elif os.path.isfile(path):
            if -1 !=  path.rfind(".cpp"):
                directoryList['cpp'].append(path)
                print("search file: %s"%path)
            elif -1 != path.rfind(".h"):
                directoryList['header'].append(path)
                print("search file: %s"%path)
            else:
                directoryList['other'].append(path)

def FindSourceFile(path,directoryList):
    if not path:
        print "This is not path!\n"
        return
    else:
        SearchFile(path,directoryList)
