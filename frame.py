from tkinter import *

root = Tk()
root.title('Bloques')


frame = LabelFrame(root,text='Login')
frame.pack()

l = Label(frame,text='hola')
l.pack()

btn = Button(frame,text="Salir",command=quit)
btn.pack()
root.mainloop()