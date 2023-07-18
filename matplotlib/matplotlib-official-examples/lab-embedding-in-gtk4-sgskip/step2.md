# Define the function to create the GTK4 application window

```python
def on_activate(app):
    win = Gtk.ApplicationWindow(application=app)
    win.set_default_size(400, 300)
    win.set_title("Embedding in GTK4")
```

This function defines the GTK4 application window with a default size of 400x300 and a title of "Embedding in GTK4".
