import tkinter

class myApplication:                     #1
    def __init__(self,root):
        self.root = root                 #2
        self.initialisation()            #3

    def initialisation(self):            #3
        tkinter.Label(self.root,text="Hello, world !").grid(column=0,row=0)   #4

def main():                              #5
    root = tkinter.Tk()
    root.title('My application')
    app = myApplication(root)
    root.mainloop()

if __name__ == "__main__":
    main()

# Source: https://sebsauvage.net/python/snyppets/#tkinter_tips

#1 : It's always better to code a GUI in the form of a class. It will be easier to reuse your GUI components.

#2 : Always keep a reference to your ancestor. You will need it when adding widgets.

#3 : Keep the code which creates all the widgets clearly separated from the rest of the code. It will be easier to maintain.

#4 : Do not use the .pack(). It's usually messy, and painfull when you want to extend your GUI. grid() lets you place and move your widgets elements easily. Never ever mix .pack() and .grid(), or your application will hang without warning, with 100% CPU usage.

#5 : It's always a good idea to have a main() defined. This way, you can test the GUI elements by directly by running the module.
