import tkinter as tk
from tkinter import filedialog
from tkinter import *

onGreen = '#%02x%02x%02x' % (64, 255, 16)
offGray = '#%02x%02x%02x' % (64, 48, 32)

class testApp:

    def __init__(self, master):
        self.master = master
        master.title("Test")
        self.createWidgets(master)

        self.indicator.create_rectangle(2,2,33,33, fill=offGray)
        for item in ['Bob', 'Jane', 'Jake', 'Ragnar', 'Sarah']:
            self.list.insert(END, item)
        for num in range(0, 100):
            self.list.insert(END, num)

    def start(self):
        self.indicator.create_rectangle(2,2,33,33, fill=onGreen)
        self.startButton.config(state = DISABLED)
        self.stopButton.config(state = NORMAL)
        print('start')

    def stop(self):
        self.indicator.create_rectangle(2,2,33,33, fill=offGray)
        self.startButton.config(state = NORMAL)
        self.stopButton.config(state = DISABLED)
        print('stop')

    def addUser(self):
        folder_selected = filedialog.askdirectory() #check for null
        self.stop()
        self.indicator.create_rectangle(2,2,33,33, fill=offGray)
        self.startButton.config(state = DISABLED)
        self.trainButton.config(state = NORMAL)
        print('add user ' + folder_selected)

    def removeUser(self):
        self.stop()
        self.indicator.create_rectangle(2,2,33,33, fill=offGray)
        self.startButton.config(state = DISABLED)
        self.trainButton.config(state = NORMAL)
        print('remove user')

    def train(self):
        self.startButton.config(state = NORMAL)
        print('train')

    def createWidgets(self, master):
        self.addButton = Button(master, text='Add User', command=self.addUser)
        self.addButton.grid(column=0, row=0, padx=(4,2))

        self.removeButton = Button(master, text='Remove User', command=self.removeUser)
        self.removeButton.grid(column=1, row=0, padx=(2,4))

        self.trainButton = Button(master, text='Train', state=DISABLED, command=self.train)
        self.trainButton.grid(column=0, row=1)

        self.startButton = Button(master, text='Start', command=self.start)
        self.startButton.grid(column=0, row=7)

        self.stopButton = Button(master, text='Stop', state=DISABLED, command=self.stop)
        self.stopButton.grid(column=1, row=7)

        self.indicator = Canvas(master, width=32, height=32)
        self.indicator.grid(column=0, row=6)

        self.list = Listbox(master, width=16, height=10)
        self.list.grid(column=2, row=0, rowspan=8)

        self.scroll = Scrollbar(master, orient="vertical")
        self.scroll.config(command=self.list.yview)
        self.scroll.grid(column=3, row=0, rowspan=8, sticky="ns")

root = Tk()
my_gui = testApp(root)
root.mainloop()