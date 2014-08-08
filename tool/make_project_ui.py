#!/usr/bin/env python
# coding=utf-8

import Tkinter
import tkFileDialog
import SearchFile 

top     =None
dirList =None 
E1      =None

def init_top(top):
    top.title("make project file")
    top.maxsize(400,160)
    top.minsize(400,160)
    
    
def OnDirectorButton():
    dialog = tkFileDialog.askdirectory()
    if not dialog:
        print("Has not select goal direction!")
    else:
        num = dirList.size()
        for it in range(0,num):
            if dialog == dirList.get(it):
                dirList.activate(it)
                dirList.see(it) 
                print("There is the same director file(%s) in %d postion of list"%(dialog, it))
                return

        dirList.insert(Tkinter.END, dialog)
        dirList.see(Tkinter.END)
        print("add directory: %s to list"%dialog)   

def OnOk():
    projectfile = E1.get()
    if not projectfile:
        print("Please key project file name!")
        return

    directoryList = {'cpp':[],'header':[],'other':[]} 
    num = dirList.size()
    print("dirlist size: %d"%num)
    for it in range(0,num):
        print "Direcotry file:" + dirList.get(it)
        SearchFile.FindSourceFile(dirList.get(it), directoryList)
    
    try:
        fPro = open(projectfile, 'w')
    except IOError:
        print("open file: %s failure!"%projectfile)
        top.quit()
    else:
        print("start makeing project file -----------------------------")
        fPro.write("SOURCES += \\\n")
        for cpp in directoryList['cpp']:
            fPro.write(cpp+"\\\n")
            print("write file: %s"%cpp)

        fPro.write("\n\n")    
        fPro.write("HEADERS += \\\n")
        for h in directoryList['header']:
            fPro.write(h+"\\\n")
            print("write file: %s"%h)
            
        fPro.write("\n\n")    
        fPro.write("OTHER_FILES += \\\n")
        for o in directoryList['other']:
            fPro.write(o+"\\\n")
            print("write file: %s"%o)
    
        top.quit()
        print("Finished making project file ---------------------------")

top = Tkinter.Tk()
init_top(top)
btn = Tkinter.Button(top, text = "Open",bd = 4, command = OnDirectorButton)
btn.pack()
btn.place(bordermode=Tkinter.OUTSIDE,height = 50, width = 100, x=0, y=0)
dirList = Tkinter.Listbox(top,bd = 4)
dirList.pack()
dirList.place(height = 50, width = 300,x = 100, y =0)
#dirList.yview()

L1 = Tkinter.Label(top,text = "Project name:")
L1.pack()
L1.place(height = 40, width = 100, x = 0, y = 60)
E1 = Tkinter.Entry(top, bd = 4)
E1.pack()
E1.place(height = 40, width = 300, x = 100, y = 60)

btnOk = Tkinter.Button(top, text = "OK", bd = 4, command = OnOk)
btnOk.pack()
btnOk.place(height = 40, width = 100, x = 80, y = 110)

btnCancel = Tkinter.Button(top, text = "Cancel", bd = 4, command = top.quit)
btnCancel.pack()
btnCancel.place(height = 40, width = 100, x = 220, y = 110)

top.mainloop()


