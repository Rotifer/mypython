# Eramo Notes

My notes taken from the Tkinter course


## Links

- [Github source code](https://github.com/PacktPublishing/The-Art-of-Doing-Create-10-Python-GUIs-with-Tkinter-Today)
- [Icon Archive](https://iconarchive.com)

```{python}
```

## Chapter 1

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

- basics1_labels_and_pack.py


