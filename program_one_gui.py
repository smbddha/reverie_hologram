import Tkinter
from Tkinter import *
from ttk import *
import Tkconstants, tkFileDialog
import csv



class App(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.output()

        # options for buttons
        button_opt = {'fill': Tkconstants.BOTH, 'padx': 5, 'pady': 5}

        # define buttons
        Tkinter.Button(self, text='Open File', command=self.askopenfile).pack(**button_opt)
        Tkinter.Button(self, text='Open Filename', command=self.askopenfilename).pack(**button_opt)
        Tkinter.Button(self, text='Save File', command=self.asksaveasfile).pack(**button_opt)
        Tkinter.Button(self, text='Save Filename', command=self.asksaveasfilename).pack(**button_opt)

        # define options for opening or saving a file
        self.file_opt = options = {}
        options['defaultextension'] = '.txt'
        options['filetypes'] = [('all files', '.*'), ('text files', '.txt')]
        options['initialdir'] = 'C:\\'
        options['initialfile'] = 'reverie_settings.txt'
        options['parent'] = root
        options['title'] = 'This is a title'

        # This is only available on the Macintosh, and only when Navigation Services are installed.
        #options['message'] = 'message'

        # if you use the multiple file version of the module functions this option is set automatically.
        #options['multiple'] = 1

        # defining options for opening a directory
        self.dir_opt = options = {}
        options['initialdir'] = 'C:\\'
        options['mustexist'] = False
        options['parent'] = root
        options['title'] = 'This is a title'

    def askopenfile(self):

        """Returns an opened file in read mode."""

        return tkFileDialog.askopenfile(mode='r', **self.file_opt)

    def askopenfilename(self):

        """Returns an opened file in read mode.
        This time the dialog just returns a filename and the file is opened by your own code.
        """

        # get filename
        filename = tkFileDialog.askopenfilename(**self.file_opt)

        # open file on your own
        if filename:
          return open(filename, 'r')

    def asksaveasfile(self):

        """Returns an opened file in write mode."""

        return tkFileDialog.asksaveasfile(mode='w', **self.file_opt)

    def asksaveasfilename(self):

        """Returns an opened file in write mode.
        This time the dialog just returns a filename and the file is opened by your own code.
        """

        # get filename
        filename = tkFileDialog.asksaveasfilename(**self.file_opt)

        # open file on your own
        if filename:
          return open(filename, 'w')

    def output(self):
        Label(text='Projector IP:').pack(side=LEFT,padx=5,pady=5)
        self.IP = Entry(root, width=10)
        self.IP.pack(side=LEFT,padx=5,pady=5)

        Label(text='Projector Palatte:').pack(side=LEFT,padx=5,pady=5)
        self.palatte = Entry(root, width=10)
        self.palatte.pack(side=LEFT,padx=5,pady=5)

        Label(text='DMX Channel:').pack(side=LEFT,padx=5,pady=10)
        self.w = Scale(root, orient=HORIZONTAL,from_=0,to=1000)
        self.w.pack(side=LEFT, padx=5, pady=10)

        self.b = Button(root, text='Submit', command=self.writeToFile)
        self.b.pack(side=RIGHT,padx=5,pady=5)

    def writeToFile(self):
        with open('Settings.csv', 'a') as f:
            w=csv.writer(f, quoting=csv.QUOTE_ALL)
            w.writerow([self.IP.get()])
            w.writerow([self.palatte.get()])
            w.writerow([self.w.get()])




if __name__ == "__main__":
    root=Tk()
    root.configure(background='orange')
    root.title('Reverie Program 1')
    root.geometry('1000x1000')
    app=App(master=root)
    app.mainloop()
    root.mainloop()
