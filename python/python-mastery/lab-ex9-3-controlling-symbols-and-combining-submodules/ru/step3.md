# Экспорт Весьма

В `structly/__init__.py` определите переменную `__all__`, которая содержит все экспортируемые символы. После этого вы должны быть в состоянии дальнейше упростить файл `stock.py`:

```python
# stock.py

from structly import *

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
    portfolio = read_csv_as_instances('portfolio.csv', Stock)
    formatter = create_formatter('text')
    print_table(portfolio, ['name','shares','price'], formatter)
```

Кстати, использование инструкции `from module import *` в общем не пользуется популярностью в сообществе Python - особенно если вы не уверены, что делаете. Тем не менее, бывают ситуации, когда это имеет смысл. Например, если пакет определяет большое количество часто используемых символов или констант, то его использование может быть полезным.
