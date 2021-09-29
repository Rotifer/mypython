# Eramo Notes

My notes taken from the Tkinter course


## Links

- [Github source code](https://github.com/PacktPublishing/The-Art-of-Doing-Create-10-Python-GUIs-with-Tkinter-Today)
- [Icon Archive](https://iconarchive.com)

```{python}
```

## Chapter 2 - Basics

### Basic steps

All Tkinter GUI creation involves these three steps:

1. Import tkinter
2. Create  root window by calling the _tkinter_ _Tk()_ method
3. Call the _mainloop_ method on the root


### Useful methods and options of _root_

- _iconbitmap_ - set a non-defalt icon that appears in the GUI top left Has to be a _.ico_ file type
- Size the window with the _geometry_ method passing a string in the format __"500x500"__
- Set a title with the _title_ method
- Use the _resizeable_ method to determine if the window is resizable in either X or Y direction (two options: 0 or 1)
- Set _root_'s options using its _config_ method: _root.config(bg='white')_
- Create a second toplevel window by calling the _toplevel_ method of _tkinter_


### Labels and _pack_

__basics1_labels_and_pack.py__

- Create widgets by calling a _tkinter_ method that uses the capitalised version of the widget name - _tkinter.Label(..._
- Pass the root instance, frame or toplevel window instance as the first argument to the method
- Creating the method does __not__ display it on the GUI
- To display, you you need to call a __geometry manager__ method (_pack_ or _grid_) on the widget
- Can set a lot of options when creating the widget. For _Lable_ options include: _text_, _font_, _bg_.
- The _pack_ geometry manager has complex behaviour and often confusing behaviour. See eample:

#### _fill_ versus _expand_

[source](https://stackoverflow.com/questions/28089942/difference-between-fill-and-expand-options-for-tkinter-pack-method/28090362)

_fill_ tells the widget to grow to as much space is available for it in the direction specified, _expand_ tells the master to 
take any space that is not assigned to any widget and distribute it to all widgets that have a non-zero expand value

### Buttons and _grid_

__basics2_buttons_and_grid.py__

- Change a button's appearance when active  (_ activebackground="#ff0000"_ ) Does this work for other widgets?
- The _stcky_ option for the _grid_ geometry manager _ button.grid(row=1, column=0, columnspan=3, sticky="WE")  _


### Frames

- A frame is a container for other widgets
- You cannot mix _pack_ and _grid_ in the same root window, toplevel window or frame
- However, they can be used in the same GUI provided that they are used in different containers
- __FrameLabel__: a special type of _Frame_ witha border and a caption: _tkinter.LabelFrame(root, text='Grid system rules!', borderwidth=5)_


### Entry and functions

- Use _Entry_ to get a single line of input
- Use the _Entry_ _delete_ method to remove entered text
- For input and output, one approach is to create separate frames for each that contain the inputs and outputs, respectively
- Review _grid_propagate_ and _pack_propagate_ : __input_frame.grid_propagate(0)__
- To assign an action to a button click set its _command_ option to a named function or a __lambda__
- When the function needs values, wrap the function assigned to the _command_ option in a lambda


### Radiobuttons

- A set of radiobuttons act as a group
- To show that a group of radiobuttons are related, put all of the group in their own frame
- Create a string or numeric variable by calling tkinter's __StrVar()__ or __IntVar()__ and assign to a variable
- Set a value for the variable by calling its _set_ method
- Set the _variable_ option in the _Radiobutton_ constructor to the name of the variable for all of the radiobuttons in the group
- Set different values for each radiobutton by setting the _value_ option in the _Radiobutton_ constructor

```{python}
number = IntVar()
number.set(1)
radio_1 = tkinter.Radiobutton(input_frame, text='Print the number one!', variable=number, value=1)
radio_2 = tkinter.Radiobutton(input_frame, text="Print the number two!", variable=number, value=2)
```

### Images

- Easier to use PNGs than JPEGs
- For PNGs, create a Tkinter image object: _img = tkinter.PhotoImage(file='image_file.png)_
- Add the image object to a Tkinter widget: _lbl = tkinter.Label(root, image=imge)_
- For JPEGs, first have to use __ImageTk__ from __PIL__:

```{python}
image = ImageTk.PhotoImage(Image.open('file.jpg'))
label = tkinter.Label(root, image=image)
```

## Chapter 3 - Hello World GUI

Choose colours using a colour scheme generation:

[Color scheme generation](https://coolors.co)

The use of radiobuttons is exemplified here

- Create an IntVar or StringVar instance - refer to this as the __control variable__
- Create a group of radiobuttons
- Set all members of the group the to share the same control variable by setting the _variable_ option
- Use the control variable's _get_ and _set_ methods to assign and retrieve its value


