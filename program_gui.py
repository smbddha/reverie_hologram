import Tkinter
from Tkinter import *
import Tkconstants, tkFileDialog
import numpy as np
from scipy import stats
from random import randint


# Circle Movement
class Track:
    def __init__(self, canvas, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

        self.canvas = canvas
        self.ball = canvas.create_oval(self.x1, self.y1, self.x2, self.y2, fill="white", outline="#D26969", width=2)

# Just For Demonstration
    def move_ball(self):
        deltax = randint(0,5)
        deltay = randint(0,5)
        fpob.config(text="ON")
        self.canvas.move(self.ball, deltax, deltay)
        self.canvas.after(50, self.move_ball)

class GUI(Frame):

    # Choose File
    def askopenfilename(self):

        # Choose Filename
        filename = tkFileDialog.askopenfilename(**self.file_opt)

        # Open File
        if filename:
          fileroot = filename
          self.fp.config(text=fileroot)
          print(fileroot)
          return open(filename, 'r')

    # Define Main Frame
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()

        # File Choosing Labels
        self.mtd = Label(self, text="Motion Tracking Data:", fg="#CED6DE", bg="#34495e", font=("Avenir", 24)).pack(fill="x")
        self.choose = Tkinter.Button(self, text='Choose', width=9, highlightbackground="#34495e", command=self.askopenfilename).pack(fill="x")

        # File Path (Once Chosen)
        self.fp = Label(self,text='',fg="white", bg="#34495e")
        self.fp.pack(fill='x')

        # File Path Types
        self.file_opt = options = {}
        options['defaultextension'] = '.txt'
        options['filetypes'] = [('all files', '.*'), ('text files', '.png'), ('text files', '.mov')]
        options['initialdir'] = 'C:\\'
        options['initialfile'] = 'reverie_settings.txt'
        options['parent'] = root
        options['title'] = 'This is a title'



if __name__ == "__main__":

    root=Tk()

    # Window Options
    root.configure(background="#34495e")
    root.title('Reverie')
    root.geometry('350x650')
    app=GUI(master=root)

    # Live Feed Labels
    lt = Label(root, text="Live Track", fg="white", bg="#34495e", font=("Avenir", 36)).pack(fill=BOTH)
    coord = Label(root, text="Coordinates", fg="#CED6DE", bg="#34495e", font=("Avenir", 24)).pack(fill=BOTH)
    canvas = Canvas(root, width = 300, height = 300)
    canvas.pack()
    fgo = Label(root, text="Fog Output:", fg="#CED6DE", bg="#34495e", font=("Avenir", 24)).pack(fill=BOTH)
    fpob = Label(root, text='', fg="#E9AF97", font=("Avenir", 24), bg="#34495e")
    fpob.pack(fill='x')

    # Circle Movement
    ball1 = Track(canvas, 10, 10, 30, 30)
    ball1.move_ball()

    app.mainloop()
    root.mainloop()
