from tkinter import *

root = Tk()

root.title('Hola Mundo') #Titulo de la ventana
root.geometry('400x400')


#Escribir texto en la ventana. Siempre se aclara primero como variable la ventana
'''
label = Label(root,text="Hola mundo! Mi primera etiqueta")
label.pack()
o
'''
# Label(root,text="Hola mundo! Mi primera etiqueta").pack() #Por ser un lenguaje orientado a objetos.
label1 = Label(root,text="Soy malo en el TFT")
label1.grid(row=0,column=0)

root.mainloop() 