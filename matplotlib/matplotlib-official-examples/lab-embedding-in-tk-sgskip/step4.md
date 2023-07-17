# Add a Toolbar and Quit Button

We add a navigation toolbar that allows the user to zoom in and out of the plot and save it. We also add a button that closes the GUI when clicked.

```python
toolbar = NavigationToolbar2Tk(canvas, root, pack_toolbar=False)
toolbar.update()

button_quit = tkinter.Button(master=root, text="Quit", command=root.destroy)
```
