# Usando um Callable para o Formatador

Em vez de passar uma função para `.Axis.set_major_formatter`, podemos usar qualquer outro callable, como uma instância de uma classe que implementa `__call__`. Neste passo, criaremos uma classe `MyFormatter` que formata as marcas de escala (tick marks) como horários.

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
