# Обновление и тестирование программы stock.py

Теперь, когда мы создали наш пакет и исправили внутренние импорты, пришло время обновить файл `stock.py`, чтобы использовать новую структуру пакета. Пакет в Python представляет собой способ организации связанных модулей вместе. Это помогает организовать код и упрощает его управление и повторное использование.

Откройте файл `stock.py` в редакторе:

```bash
# Click on stock.py in the file explorer or run:
code stock.py
```

Текущие импорты в файле `stock.py` основаны на старой структуре, когда все файлы находились в одном каталоге. В Python, когда вы импортируете модуль, Python ищет этот модуль в определенных местах. В старой структуре, так как все файлы были в одном каталоге, Python мог легко найти модули. Но теперь, с новой структурой пакета, нам нужно обновить импорты, чтобы сообщить Python, где найти модули внутри пакета `structly`.

Обновите файл `stock.py` так, чтобы он выглядел точно так же:

```python
# stock.py

from structly.structure import Structure, String, PositiveInteger, PositiveFloat

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

Основные изменения:

1. Изменено `from structure import Structure, String, PositiveInteger, PositiveFloat` на `from structly.structure import Structure, String, PositiveInteger, PositiveFloat`. Это изменение сообщает Python искать модуль `structure` внутри пакета `structly`.
2. Изменено `from reader import read_csv_as_instances` на `from structly.reader import read_csv_as_instances`. Аналогично, это изменение направляет Python искать модуль `reader` внутри пакета `structly`.
3. Изменено `from tableformat import create_formatter, print_table` на `from structly.tableformat import create_formatter, print_table`. Это гарантирует, что Python найдет модуль `tableformat` в пакете `structly`.

Сохраните файл после внесения этих изменений. Сохранение файла важно, так как оно обеспечивает сохранение внесенных изменений и их использование при запуске программы.

Теперь давайте протестируем обновленный код, чтобы убедиться, что все работает правильно:

```bash
python stock.py
```

Вы должны увидеть следующий вывод:

```
      name      shares       price
---------- ---------- ----------
      MSFT        100      51.23
       IBM         50       91.1
      AAPL         75     145.89
      ACME        125     123.45
       HPE         75       32.2
```

Если вы видите такой вывод, поздравляем! Вы успешно создали пакет Python и обновили свой код для его использования. Это означает, что ваш код теперь организован более модульно, что облегчает его поддержку и расширение в будущем.
