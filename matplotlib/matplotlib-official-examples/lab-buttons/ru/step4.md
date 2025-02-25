# Создаем кнопки "Next" (Далее) и "Previous" (Предыдущая)

Теперь создадим кнопки "Next" (Далее) и "Previous" (Предыдущая) с использованием функции `add_axes` из `matplotlib.pyplot`, и присвоим им ранее созданные функции обратного вызова с использованием `on_clicked`.

```python
axprev = fig.add_axes([0.7, 0.05, 0.1, 0.075])
axnext = fig.add_axes([0.81, 0.05, 0.1, 0.075])
bnext = Button(axnext, 'Next')
bnext.on_clicked(callback.next)
bprev = Button(axprev, 'Previous')
bprev.on_clicked(callback.prev)
```
