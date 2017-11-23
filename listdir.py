import os
from tkinter import *
import time


class DirList(object):

    def __init__(self):
        self.top = Tk()
        self.label = Label(self.top, text='directory lister')
        self.label.pack()
        self.cwd = StringVar(self.top)

        self.dirl = Label(self.top)
        self.dirl.pack()

        self.frame = Frame(self.top)
        self.scrollbar = Scrollbar(self.frame)
        self.scrollbar.pack(side=RIGHT, fill=Y)
        self.dirlist = Listbox(self.frame, height=15,
                               width=50,
                               yscrollcommand=self.scrollbar.set)
        self.dirlist.bind('<Double-1>', self.godir)
        self.dirlist.pack(side=LEFT, fill=BOTH)
        self.scrollbar.config(command=self.dirlist.yview)
        self.frame.pack()
        
        self.cwd.set(os.getcwd())
        self.doLS()

    def doLS(self, ev=None):
        tdir = self.cwd.get()
        self.dirl.config(text=tdir)
        ls = os.listdir(tdir)
        self.dirlist.delete(0, END)
        self.dirlist.insert(END, os.curdir)
        self.dirlist.insert(END, os.pardir)
        for dir in ls:
            self.dirlist.insert(END, dir)
    def godir(self, ev=None):
        tdir = self.dirlist.get(self.dirlist.curselection())
        if os.path.isdir(tdir):
            pth = os.path.join(self.cwd.get(), tdir+'/')
            os.chdir(pth)
            self.cwd.set(os.getcwd())
            self.doLS()
        else:
            file = open(tdir, 'r')
            self.dirlist.delete(0, END)
            for line in file:
                self.dirlist.insert(END, line)


def main():
    dirlist = DirList()
    mainloop()


if __name__ == '__main__':
    main()
