# Разделение Модуля

Файл `structly/tableformat.py` содержит код для создания таблиц в различных форматах. Specifically:

- Базовый класс `TableFormatter`.
- Класс `TextTableFormatter`.
- Класс `CSVTableFormatter`.
- Класс `HTMLTableFormatter`.

Вместо того, чтобы все эти классы были в одном `.py` файле, может быть имеет смысл переместить каждый конкретный форматтер в свой собственный файл. Для этого мы собираемся разделить файл `tableformat.py` на части. Следуйте инструкциям внимательно:

Во - первых, удалите директорию `structly/__pycache__`.

    % cd structly
    % rm -rf __pycache__

Далее, создайте директорию `structly/tableformat`. Эта директория должна иметь точно такое же имя, как и модуль, который она заменяет (`tableformat.py`).

```bash
mkdir tableformat
```

Переместите исходный файл `tableformat.py` в новую директорию `tableformat` и переименуйте его в `formatter.py`.

```bash
mv tableformat.py tableformat/formatter.py
```

В директории `tableformat` разделите код `tableformat.py` на следующие файлы и директории:

- `formatter.py` - Содержит базовый класс `TableFormatter`, миксины и различные функции.
- `formats/text.py` - Содержит класс `TextTableFormatter`.
- `formats/csv.py` - Содержит класс `CSVTableFormatter`.
- `formats/html.py` - Содержит класс `HTMLTableFormatter`.

Добавьте файл `__init__.py` в директории `tableformat/` и `tableformat/formats`. Пусть `tableformat/__init__.py` экспортирует те же символы, что и исходный файл `tableformat.py`.

После того, как вы сделаете все эти изменения, у вас должна быть структура пакета, которая выглядит так:

    structly/
          __init__.py
          validate.py
          reader.py
          structure.py
          tableformat/
               __init__.py
               formatter.py
               formats/
                   __init__.py
                   text.py
                   csv.py
                   html.py

Для пользователей все должно работать точно так же, как и раньше. Например, ваш предыдущий файл `stock.py` должен работать:

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

    def sell(self, nshares):
        self.shares -= nshares

if __name__ == '__main__':
    portfolio = read_csv_as_instances('portfolio.csv', Stock)
    formatter = create_formatter('text')
    print_table(portfolio, ['name','shares','price'], formatter)
```
