# Управление Экспортируемыми Символами

Измените все подмодули в пакете `structly` так, чтобы они явно определяли переменную `__all__`, которая экспортирует выбранные символы. Specifically:

- `structure.py` должен экспортировать `Structure`
- `reader.py` должен экспортировать все различные функции `read_csv_as_*()`
- `tableformat.py` экспортирует `create_formatter()` и `print_table()`

Теперь, в файле `__init__.py`, объедините все подмодули так:

```python
# structly/__init__.py

from.structure import *
from.reader import *
from.tableformat import *
```

После этого вы должны быть в состоянии импортировать все из одного логического модуля:

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
