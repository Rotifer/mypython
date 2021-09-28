from tkinter import *
  
root = Tk()
lbl = Label(root, text ="Hello World")
btn = Button(root, text="Exit", command=root.destroy)
lbl.pack()
btn.pack()
root.mainloop()
