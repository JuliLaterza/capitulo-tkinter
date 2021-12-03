from tkinter import *

root = Tk()
root.title('Probando botones')


l = Label(root,text="Hola mundo",fg='blue') #Si la agrego antes de la función, no se agrega infinito
def click():
    l.pack()


btn = Button(root,text="Clic acá", command=click, fg='white',bg='black')

btn.pack()

root.mainloop()