import tkinter as tk
from tkinter import ttk
import PIL
import sys
print(sys.executable)

class SQLiteManager(tk.Frame):
    """GUI for managing SQLite databases
    """
    def __init__(self, parent, *args, **kwargs):
        """Initialise with a root window
        """
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.parent.geometry('2000x2000')
        self.parent.resizable(0,0)
        #<create the rest of your GUI here>

    def _add_buttons(self):
        """Add file open dialog
        """
if __name__ == "__main__":
    root = tk.Tk()
    SQLiteManager(root).pack(side="top", fill="both", expand=True)
    root.mainloop()
