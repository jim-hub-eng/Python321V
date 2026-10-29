from tkinter import *

root = Tk()

myLabelL1 = Label(root, text= "Hola Mundo")
myLabelL2 = Label(root, text="Mi nombre es Jim")
myLabelL3 = Label(root, text="Columan 3")
myLabelL4 = Label(root, text="Columna 4")
myLabelL5 = Label(root, text="Columna 5")

myLabelL1.grid(row=0, column=0)
myLabelL2.grid(row=1, column=0)
myLabelL3.grid(row=2, column=0)
myLabelL4.grid(row=3, column=0)
myLabelL5.grid(row=4, column=0)

root.mainloop()