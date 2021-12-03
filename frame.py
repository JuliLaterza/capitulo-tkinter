from tkinter import *

root = Tk()
root.title('Bloques')
root.geometry('200x200')

# frame = LabelFrame(root,text='Login',padx=20,pady=15,borderwidth=4) Si le dejamos el "TEXT" se queda en el cuadradito

frame = LabelFrame(root,padx=20,pady=15,borderwidth=4) #Para hacer box
frame.pack(pady=20,padx=20)

l = Label(frame,text='Caja')
l.pack(padx=10,pady=10)

btn = Button(frame,text="Salir",command=quit,pady=10,padx=10 )
btn.pack()
root.mainloop()