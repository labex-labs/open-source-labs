# Добавляем метку на холст

```python
label = Gtk.Label()
label.set_markup('Drag mouse over axes for position')
vbox.insert_child_after(label, fig.canvas)
```

Мы создаем метку и задаем ее текст. Добавляем метку в vbox после холста фигуры.
