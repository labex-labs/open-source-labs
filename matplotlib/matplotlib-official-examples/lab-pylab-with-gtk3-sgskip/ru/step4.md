# Добавление кнопки на панель инструментов

Мы добавим кнопку на панель инструментов с использованием модуля Gtk. Во - первых, мы создаем кнопку с надписью и подключаем ее к функции, которая выводит сообщение при нажатии. Затем мы создаем элемент инструмента, задаем ему текст подсказки, добавляем кнопку в него и вставляем его в панель инструментов.

```python
button = Gtk.Button(label='Click me')
button.show()
button.connect('clicked', lambda button: print('hi mom'))

toolitem = Gtk.ToolItem()
toolitem.show()
toolitem.set_tooltip_text('Click me for fun and profit')
toolitem.add(button)

pos = 8  # где вставить это в панель инструментов
toolbar.insert(toolitem, pos)
```
