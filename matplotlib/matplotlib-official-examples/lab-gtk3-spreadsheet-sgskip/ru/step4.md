# Добавьте метку

В этом шаге мы добавим метку в окно, которая попросит пользователя двойным щелчком по строке, чтобы построить график данных.

```python
vbox = Gtk.VBox(homogeneous=False, spacing=8)
self.add(vbox)
label = Gtk.Label(label='Double click a row to plot the data')
vbox.pack_start(label, False, False, 0)
```
