# Create the Application

Create a GTK4 application and specify the window size and title.

```python
def on_activate(app):
    win = Gtk.ApplicationWindow(application=app)
    win.set_default_size(400, 300)
    win.set_title("Embedding in GTK4")
```
