from tkinter import *


#Creacion de ventana
root = Tk()
root.title('Inputs')
root.geometry('500x500')

e = Entry(root,width=40)
e.pack()
e.insert(0,"Ingresa texto: ")


def click():
    texto = e.get() #Obtengo el dato
    textVariable.set(texto)

    #l = Label(root,text=texto) #Este código sirve para hacer una lista
    #l.pack() 
    e.delete(0,END)
    #l.configure(text=texto) #Actualizo el dato

btn = Button(root, text='click',command=click)
btn.pack()

textVariable = StringVar()

l = Label(root,textvariable=textVariable)
l.pack()
#Ejecutar app
root.mainloop()