import tkinter as tk
from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image
from os import walk

onGreen = '#%02x%02x%02x' % (64, 255, 16)
offGray = '#%02x%02x%02x' % (64, 48, 32)

def populateUsers(self):
    f = []
    for (dirpath, dirnames, filenames) in walk('.\\venv\\faces\\'):
        f.extend(dirnames)
        break
    for item in f:
        self.list.insert(END, item)

class testApp:

    def __init__(self, master):
        self.master = master
        master.title("Test")
        self.createWidgets(master)
        self.indicator.create_rectangle(2,2,33,33, fill=offGray)
        populateUsers(self)

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
        self.addButton = Button(master, font=('', 14), text='Add User', command=self.addUser)
        self.addButton.grid(column=0, row=0, padx=(4,2))

        self.removeButton = Button(master, font=('', 14), text='Remove User', command=self.removeUser)
        self.removeButton.grid(column=1, row=0, padx=(2,4))

        self.trainButton = Button(master, font=('', 14), text='Train', state=DISABLED, command=self.train)
        self.trainButton.grid(column=0, row=1)

        self.startButton = Button(master, font=('', 14), text='Start', command=self.start)
        self.startButton.grid(column=0, row=7)

        self.stopButton = Button(master, font=('', 14), text='Stop', state=DISABLED, command=self.stop)
        self.stopButton.grid(column=1, row=7)

        self.title = Label(master, text='Face Recognition Lock\nCSC357 2018')
        self.title.grid(column=0, row=2, columnspan=2)

        self.img = ImageTk.PhotoImage(Image.open('.\\logo.png'))
        self.logo = Label(master, image=self.img, width=192, height=48)
        self.logo.grid(column=0, row=3, columnspan=2)

        self.credit_column_1 = Label(master, text='Amy Dixon\nCarson Williams\nJerry Malcomson')
        self.credit_column_1.grid(column=0, row=4)
        self.credit_column_2 = Label(master, text='Casey Niccum\nDerek Crew\nDevin Deneault', anchor='e')
        self.credit_column_2.grid(column=1, row=4)

        self.indicator = Canvas(master, width=32, height=32)
        self.indicator.grid(column=0, row=6)

        self.list = Listbox(master, font=('', 12), width=16, height=20)
        self.list.grid(column=2, row=0, rowspan=8)

        self.scroll = Scrollbar(master, orient='vertical')
        self.scroll.config(command=self.list.yview)
        self.scroll.grid(column=3, row=0, rowspan=8, sticky='ns')

root = Tk()
my_gui = testApp(root)
root.mainloop()