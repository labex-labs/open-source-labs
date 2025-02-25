# Добавляем кнопку на панель инструментов

```python
button = Gtk.Button(label='Click me')
button.connect('clicked', lambda button: print('hi mom'))
button.set_tooltip_text('Click me for fun and profit')
toolbar.append(button)
```

Мы создаем кнопку с надписью и подсказкой, и подключаем ее к функции, которая выводит сообщение в консоль. Добавляем кнопку на панель инструментов.
