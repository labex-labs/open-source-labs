# Использование вызываемого объекта для форматтера

Вместо передачи функции в `.Axis.set_major_formatter`, мы можем использовать любой другой вызываемый объект, такой как экземпляр класса, который реализует `__call__`. В этом шаге мы создадим класс `MyFormatter`, который будет форматировать деления на шкале времени.

```python
# Use a callable for formatter
class MyFormatter(Formatter):
    def __init__(self, dates, fmt='%a'):
        self.dates = dates
        self.fmt = fmt

    def __call__(self, x, pos=0):
        """Return the label for time x at position pos."""
        try:
            return self.dates[round(x)].item().strftime(self.fmt)
        except IndexError:
            pass

ax2.xaxis.set_major_formatter(MyFormatter(r.date, '%a'))
```
