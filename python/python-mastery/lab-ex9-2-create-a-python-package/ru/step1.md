# Создание пакета

В предыдущих практиках вы создали следующие файлы, связанные с структурированными данными с проверкой типов, чтением данных и созданием таблиц:

- `structure.py`
- `validate.py`
- `reader.py`
- `tableformat.py`

Ваша задача — взять все эти файлы и переместить их в пакет под названием `structly`. Для этого следуйте шагам:

- Создайте директорию под названием `structly`
- Создайте пустой файл `__init__.py` и поместите его в директорию `structly`
- Переместите файлы `structure.py`, `validate.py`, `reader.py` и `tableformat.py` в директорию `structly`.
- Исправьте любые инструкции импорта между модулями (в частности, модуль `structure` зависит от `validate`).

После этого измените программу `stock.py` так, чтобы она выглядела именно так и работала:

```python
# stock.py

from structly.structure import Structure

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
    from structly.reader import read_csv_as_instances
    from structly.tableformat import create_formatter, print_table
    portfolio = read_csv_as_instances('portfolio.csv', Stock)
    formatter = create_formatter('text')
    print_table(portfolio, ['name','shares','price'], formatter)
```
