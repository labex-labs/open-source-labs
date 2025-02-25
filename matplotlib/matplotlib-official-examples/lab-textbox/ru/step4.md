# Создаем виджет Textbox

Мы создаем виджет Textbox и добавляем его на рисунок. Метод `on_submit` используется для вызова функции `submit`, когда пользователь нажимает клавишу Enter в текстовом поле или покидает его. Мы также задаем начальное значение виджета Textbox равным `t ** 2`.

```python
axbox = fig.add_axes([0.1, 0.05, 0.8, 0.075])
text_box = TextBox(axbox, "Evaluate", textalignment="center")
text_box.on_submit(submit)
text_box.set_val("t ** 2")  # Trigger `submit` with the initial string.
```
