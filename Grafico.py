from Tkinter import *

root = Tk()

topFrame=Frame(root)
topFrame.pack()
bottomFrame=Frame(root)
bottomFrame.pack(side=BOTTOM)

button1 = Button(topFrame, text="boton1", fg="red")
button2 = Button(topFrame, text="boton1", fg="blue")
button3 = Button(topFrame, text="boton1", fg="green")
button4 = Button(bottomFrame, text="boton1", fg="purple")

button1.pack(side=LEFT)
button2.pack(side=LEFT)
button3.pack(side=LEFT)
button4.pack()

root.mainloop()