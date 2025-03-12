# Создание удобного для пользователя API для миксинов

Миксины (mixins) - это мощная возможность в Python, но они могут быть немного сложными для начинающих, так как они связаны с множественным наследованием, которое может стать довольно сложным. На этом этапе мы облегчим жизнь пользователям, улучшив функцию `create_formatter()`. Таким образом, пользователям не придется слишком беспокоиться о деталях множественного наследования.

Сначала вам нужно открыть файл `tableformat.py`. Это можно сделать, запустив следующие команды в терминале. Команда `cd` изменяет текущую директорию на папку проекта, а команда `code` открывает файл `tableformat.py` в редакторе кода.

```bash
cd ~/project
code tableformat.py
```

После открытия файла найдите функцию `create_formatter()`. В настоящее время она выглядит так:

```python
def create_formatter(name):
    """
    Create an appropriate formatter based on the name.
    """
    if name == 'text':
        return TextTableFormatter()
    elif name == 'csv':
        return CSVTableFormatter()
    elif name == 'html':
        return HTMLTableFormatter()
    else:
        raise RuntimeError(f'Unknown format {name}')
```

Эта функция принимает имя в качестве аргумента и возвращает соответствующий форматер. Но мы хотим сделать ее более гибкой. Мы изменим ее так, чтобы она могла принимать необязательные аргументы для наших миксинов.

Замените существующую функцию `create_formatter()` на улучшенную версию ниже. Эта новая функция позволяет указать форматы столбцов и преобразовывать заголовки в верхний регистр.

```python
def create_formatter(name, column_formats=None, upper_headers=False):
    """
    Create a formatter with optional enhancements.

    Parameters:
    name : str
        Name of the formatter ('text', 'csv', 'html')
    column_formats : list, optional
        List of format strings for column formatting
    upper_headers : bool, optional
        Whether to convert headers to uppercase
    """
    if name == 'text':
        formatter_cls = TextTableFormatter
    elif name == 'csv':
        formatter_cls = CSVTableFormatter
    elif name == 'html':
        formatter_cls = HTMLTableFormatter
    else:
        raise RuntimeError(f'Unknown format {name}')

    # Apply mixins if requested
    if column_formats and upper_headers:
        class CustomFormatter(ColumnFormatMixin, UpperHeadersMixin, formatter_cls):
            formats = column_formats
        return CustomFormatter()
    elif column_formats:
        class CustomFormatter(ColumnFormatMixin, formatter_cls):
            formats = column_formats
        return CustomFormatter()
    elif upper_headers:
        class CustomFormatter(UpperHeadersMixin, formatter_cls):
            pass
        return CustomFormatter()
    else:
        return formatter_cls()
```

Эта улучшенная функция работает следующим образом: сначала она определяет базовый класс форматера на основе аргумента `name`. Затем, в зависимости от того, были ли предоставлены `column_formats` и `upper_headers`, она создает настраиваемый класс форматера, включающий соответствующие миксины. Наконец, она возвращает экземпляр настраиваемого класса форматера.

Теперь протестируем нашу улучшенную функцию с различными комбинациями параметров.

Сначала попробуем использовать форматирование столбцов. Запустите следующую команду в терминале. Эта команда импортирует необходимые функции и данные из файла `tableformat.py`, создает форматер с форматированием столбцов и затем выводит таблицу с использованием этого форматера.

```python
python3 -c "
from tableformat import create_formatter, portfolio, print_table

formatter = create_formatter('text', column_formats=['%s', '%d', '%0.2f'])
print_table(portfolio, ['name', 'shares', 'price'], formatter)
"
```

Вы должны увидеть таблицу с отформатированными столбцами. Вывод будет выглядеть так:

```
      name     shares      price
---------- ---------- ----------
        AA        100      32.20
       IBM         50      91.10
       CAT        150      83.44
      MSFT        200      51.23
        GE         95      40.37
      MSFT         50      65.10
       IBM        100      70.44
```

Далее попробуем использовать заголовки в верхнем регистре. Запустите следующую команду:

```python
python3 -c "
from tableformat import create_formatter, portfolio, print_table

formatter = create_formatter('text', upper_headers=True)
print_table(portfolio, ['name', 'shares', 'price'], formatter)
"
```

Вы должны увидеть таблицу с заголовками в верхнем регистре. Вывод будет следующим:

```
      NAME     SHARES      PRICE
---------- ---------- ----------
        AA        100       32.2
       IBM         50       91.1
       CAT        150      83.44
      MSFT        200      51.23
        GE         95      40.37
      MSFT         50       65.1
       IBM        100      70.44
```

Наконец, объединим оба параметра. Запустите эту команду:

```python
python3 -c "
from tableformat import create_formatter, portfolio, print_table

formatter = create_formatter('text', column_formats=['%s', '%d', '%0.2f'], upper_headers=True)
print_table(portfolio, ['name', 'shares', 'price'], formatter)
"
```

Это должно отобразить таблицу с отформатированными столбцами и заголовками в верхнем регистре. Вывод будет:

```
      NAME     SHARES      PRICE
---------- ---------- ----------
        AA        100      32.20
       IBM         50      91.10
       CAT        150      83.44
      MSFT        200      51.23
        GE         95      40.37
      MSFT         50      65.10
       IBM        100      70.44
```

Улучшенная функция также работает с другими типами форматеров. Например, попробуем ее с форматером CSV. Запустите следующую команду:

```python
python3 -c "
from tableformat import create_formatter, portfolio, print_table

formatter = create_formatter('csv', column_formats=['\\"%s\\"', '%d', '%0.2f'])
print_table(portfolio, ['name', 'shares', 'price'], formatter)
"
```

Это должно сформировать вывод в формате CSV с отформатированными столбцами. Вывод будет:

```
name,shares,price
"AA",100,32.20
"IBM",50,91.10
"CAT",150,83.44
"MSFT",200,51.23
"GE",95,40.37
"MSFT",50,65.10
"IBM",100,70.44
```

Улучшив функцию `create_formatter()`, мы создали удобный для пользователя API. Теперь пользователи могут легко использовать миксины, не зная сложных деталей множественного наследования. Это дает им возможность настраивать форматеры в соответствии с их потребностями.
