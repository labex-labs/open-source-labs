# Добавление метки в VBox

Мы добавим метку в vbox для отображения координат x,y мыши, когда она перетаскивается по оси. Во - первых, мы создаем метку с некоторым текстом и добавляем ее в vbox.

```python
label = Gtk.Label()
label.set_markup('Drag mouse over axes for position')
label.show()
vbox.pack_start(label, False, False, 0)
```
