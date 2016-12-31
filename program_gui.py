import Tkinter as tk
from Tkinter import *
import Tkconstants, tkFileDialog
import numpy as np
from scipy import stats
from random import randint

# NOTE For Live Feed
# # Circle Movement
# class Track:
#     def __init__(self, canvas, x1, y1, x2, y2):
#         self.x1 = x1
#         self.y1 = y1
#         self.x2 = x2
#         self.y2 = y2
#
#         self.canvas = canvas
#         self.ball = canvas.create_oval(self.x1, self.y1, self.x2, self.y2, fill="white", outline="#D26969", width=2)
#
# # Just For Demonstration
#     def move_ball(self):
#         deltax = randint(0,5)
#         deltay = randint(0,5)
#         fpob.config(text="ON")
#         self.canvas.move(self.ball, deltax, deltay)
#         self.canvas.after(50, self.move_ball)

class Drag:


    def _create_token(self, coord, color):
        '''Create a token at the given coordinate in the given color'''
        (x,y) = coord
        self.ball = self.canvas.create_oval(x-5, y-5, x+5, y+5,
                                outline=color, fill=color, tags="token")

    def OnTokenButtonPress(self, event):
        '''Being drag of an object'''
        # record the item and its location
        self._drag_data["item"] = self.ball
        # self.canvas.find_closest(event.x, event.y)[0]
        self._drag_data["x"] = event.x
        self._drag_data["y"] = event.y

    def OnTokenButtonRelease(self, event):
        '''End drag of an object'''
        # reset the drag information
        self._drag_data["item"] = None
        self._drag_data["x"] = 0
        self._drag_data["y"] = 0

    def OnTokenMotion(self, event):
        '''Handle dragging of an object'''
        # compute how much this object has moved
        delta_x = event.x - self._drag_data["x"]
        delta_y = event.y - self._drag_data["y"]
        # move the object the appropriate amount
        self.canvas.move(self._drag_data["item"], delta_x, delta_y)
        # record the new position
        self._drag_data["x"] = event.x
        self._drag_data["y"] = event.y

        self.x_value.delete(0, 'end')
        self.x_value.insert(0,self._drag_data["x"]);
        self.y_value.delete(0, 'end')
        self.y_value.insert(0,abs(self._drag_data["y"]-255));

    def x_and_y(self):
        self.x_value_int = float(self.x_value.get())
        self.y_value_int = float(self.y_value.get())

        self.coords = self.canvas.coords(self.ball)
        self.cord_x_value = (self.coords[0] + 5)
        self.cord_y_value = (self.coords[1] + 5)
        print(self.coords)
        self.canvas.move(self.ball, self.x_value_int - self.cord_x_value+5, self.y_value_int - self.cord_y_value-5)
        # self.canvas.move(self.ball, self.cord_x_value, self.cord_y_value)
        self.x_value.delete(0, 'end')
        self.x_value.insert(0, self.x_value_int);
        self.y_value.delete(0, 'end')
        self.y_value.insert(0, abs(self.y_value_int-255));
        print(self.coords)

    def __init__(self, canvas):


        # create a canvas
        self.canvas = canvas


        # this data is used to keep track of an
        # item being dragged
        self._drag_data = {"x": 0, "y": 0, "item": None}

        # create a couple movable objects
        self._create_token((100, 100), "white")
        self._create_token((127.5, 127.5), "black")

        # add bindings for clicking, dragging and releasing over
        # any object with the "token" tag
        self.canvas.tag_bind("token", "<ButtonPress-1>", self.OnTokenButtonPress)
        self.canvas.tag_bind("token", "<ButtonRelease-1>", self.OnTokenButtonRelease)
        self.canvas.tag_bind("token", "<B1-Motion>", self.OnTokenMotion)


        self.x_value_label = Label(text='X-Value', fg="#CED6DE", bg="#34495e", font=("Avenir", 18)).pack(fill=BOTH)
        self.x_value = Entry(root, width=10)
        self.x_value.pack(padx=5,pady=5)
        self.y_value_label = Label(text='Y-Value', fg="#CED6DE", bg="#34495e", font=("Avenir", 18)).pack(fill=BOTH)
        self.y_value = Entry(root, width=10)
        self.y_value.pack(padx=5,pady=5)
        self.submit_button = tk.Button(root, text='Submit', width=9, highlightbackground="#34495e", command=self.x_and_y).pack(fill="x")



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
        self.choose = tk.Button(self, text='Choose', width=9, highlightbackground="#34495e", command=self.askopenfilename).pack(fill="x")

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


    canvas = Canvas(root, width = 255, height = 255)
    canvas.pack()
    drag = Drag(canvas);



    fgo = Label(root, text="Fog Output:", fg="#CED6DE", bg="#34495e", font=("Avenir", 24)).pack(fill=BOTH)
    fpob = Label(root, text='', fg="#E9AF97", font=("Avenir", 24), bg="#34495e")
    fpob.pack(fill='x')


    # NOTE For Live Feed
    # # Circle Movement
    # ball1 = Track(canvas, 10, 10, 30, 30)
    # ball1.move_ball()

    app.mainloop()
    root.mainloop()

# from Tkinter import *
#
# master = Tk()
#
# e = Entry(master)
# e.pack()
#
# e.focus_set()
#
# def callback():
#     print e.get()
#
# b = Button(master, text="get", width=10, command=callback)
# b.pack()
#
# mainloop()
# e = Entry(master, width=50)
# e.pack()
#
# text = e.get()
# def makeentry(parent, caption, width=None, **options):
#     Label(parent, text=caption).pack(side=LEFT)
#     entry = Entry(parent, **options)
#     if width:
#         entry.config(width=width)
#     entry.pack(side=LEFT)
#     return entry
#
# user = makeentry(parent, "User name:", 10)
# password = makeentry(parent, "Password:", 10, show="*")
# content = StringVar()
# entry = Entry(parent, text=caption, textvariable=content)
#
# text = content.get()
# content.set(text)
