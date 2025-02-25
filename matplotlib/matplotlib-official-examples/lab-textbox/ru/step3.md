# Определяем функцию submit

Мы определяем функцию `submit`, которая будет вызываться, когда пользователь отправляет текстовый ввод. Эта функция обновляет отображаемую функцию в зависимости от ввода пользователя.

```python
def submit(expression):
    """
    Update the plotted function to the new math *expression*.

    *expression* is a string using "t" as its independent variable, e.g.
    "t ** 3".
    """
    ydata = eval(expression, {'np': np}, {'t': t})
    l.set_ydata(ydata)
    ax.relim()
    ax.autoscale_view()
    plt.draw()
```
