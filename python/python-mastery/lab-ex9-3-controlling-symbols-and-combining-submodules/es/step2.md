# Control de los Símbolos Exportados

Modifica todos los submódulos del paquete `structly` de modo que definan explícitamente una variable `__all__` que exporte los símbolos seleccionados. Específicamente:

- `structure.py` debe exportar `Structure`
- `reader.py` debe exportar todas las funciones `read_csv_as_*()`
- `tableformat.py` exporta `create_formatter()` y `print_table()`

Ahora, en el archivo `__init__.py`, unifica todos los submódulos de la siguiente manera:

```python
# structly/__init__.py

from.structure import *
from.reader import *
from.tableformat import *
```

Una vez que hayas hecho esto, deberías poder importar todo desde un solo módulo lógico:

```python
# stock.py

from structly import Structure

class Stock(Structure):
    name = String()
    shares = PositiveInteger()
    price = PositiveFloat()

    @property
    def cost(self):
        return self.shares * self.price

    def sell(self, nshares: PositiveInteger):
        self.shares -= nshares

if __name__ == '__main__':
    from structly import read_csv_as_instances, create_formatter, print_table
    portfolio = read_csv_as_instances('portfolio.csv', Stock)
    formatter = create_formatter('text')
    print_table(portfolio, ['name','shares','price'], formatter)
```
