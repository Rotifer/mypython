# Simple combobox demo
import tkinter
import os
from tkinter import ttk, END

#Define window
root = tkinter.Tk()
root.title('Environment Variables')
root.iconbitmap('ruler.ico')
root.resizable(0,0)

env = dict(os.environ)
env_keys =  sorted(list(env.keys()))

def get_env_val():
    env_var = cbox.get()
    env_val = env.get(env_var, 'No such key')
    txt.delete(0, END)
    txt.insert(0, env_val)

cbox = ttk.Combobox(root, value=env_keys)
txt = tkinter.Entry(root)
cbox.grid(row=0, column=0)
txt.grid(row=0,column=1)
btn = tkinter.Button(root, text='Get', command=lambda:get_env_val())
btn.grid(row=0, column=3)
root.mainloop()

