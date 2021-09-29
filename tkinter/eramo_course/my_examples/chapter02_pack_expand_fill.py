import Tkinter as tk

root = tk.Tk()
root.geometry('200x200+200+200')

tk.Label(root, text='Label', bg='green').pack(expand=1, fill=tk.Y)
tk.Label(root, text='Label2', bg='red').pack(fill=tk.BOTH)

root.mainloop()

