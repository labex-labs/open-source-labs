# Импортируем Matplotlib и определяем функцию on_close

В этом шаге мы импортируем Matplotlib и определяем функцию `on_close`, которая будет вызываться при закрытии фигуры. Функция просто выведет сообщение в консоль.

```python
import matplotlib.pyplot as plt

def on_close(event):
    print('Closed Figure!')
```
