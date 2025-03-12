# Создание базового класса и модификация функции вывода

В программировании наследование представляет собой мощную концепцию, которая позволяет создавать иерархию классов. Чтобы начать использовать наследование для вывода данных в различных форматах, сначала нужно создать базовый класс. Базовый класс служит шаблоном для других классов, определяя общий набор методов, которые его подклассы могут наследовать и переопределять.

Теперь создадим базовый класс, который определит интерфейс для всех форматеров таблиц. Откройте файл `tableformat.py` в WebIDE и добавьте следующий код в начало файла:

```python
class TableFormatter:
    """
    Base class for all table formatters.
    This class defines the interface that all formatters must implement.
    """
    def headings(self, headers):
        """
        Generate the table headings.
        """
        raise NotImplementedError()

    def row(self, rowdata):
        """
        Generate a single row of table data.
        """
        raise NotImplementedError()
```

Класс `TableFormatter` является абстрактным базовым классом. Абстрактный базовый класс - это класс, который определяет методы, но не предоставляет их реализаций. Вместо этого он ожидает, что его подклассы предоставят эти реализации. Исключения `NotImplementedError` используются для указания на то, что эти методы должны быть переопределены подклассами. Если подкласс не переопределит эти методы и мы попытаемся их использовать, будет вызвано исключение.

Далее нужно модифицировать функцию `print_table()` для использования класса `TableFormatter`. Функция `print_table()` используется для вывода таблицы данных из списка объектов. Модифицируя ее для использования класса `TableFormatter`, мы можем сделать функцию более гибкой и способной работать с разными форматами таблиц.

Замените существующую функцию `print_table()` следующим кодом:

```python
def print_table(records, fields, formatter):
    """
    Print a table of data from a list of objects using the specified formatter.

    Args:
        records: A list of objects
        fields: A list of field names
        formatter: A TableFormatter object
    """
    formatter.headings(fields)
    for r in records:
        rowdata = [getattr(r, fieldname) for fieldname in fields]
        formatter.row(rowdata)
```

Основное изменение здесь заключается в том, что функция `print_table()` теперь принимает параметр `formatter`, который должен быть экземпляром класса `TableFormatter` или его подкласса. Это означает, что мы можем передавать разные форматеры таблиц в функцию `print_table()`, и она будет использовать соответствующий форматер для вывода таблицы. Функция делегирует ответственность за форматирование объекту - форматеру, вызывая его методы `headings()` и `row()`.

Протестируем наши изменения, попробовав использовать базовый класс `TableFormatter`:

```python
import stock
import reader
import tableformat

portfolio = reader.read_csv_as_instances('portfolio.csv', stock.Stock)
formatter = tableformat.TableFormatter()
tableformat.print_table(portfolio, ['name', 'shares', 'price'], formatter)
```

При запуске этого кода вы должны увидеть ошибку:

```
Traceback (most recent call last):
...
NotImplementedError
```

Эта ошибка возникает потому, что мы пытаемся напрямую использовать абстрактный базовый класс, но он не предоставляет реализаций для своих методов. Поскольку методы `headings()` и `row()` в классе `TableFormatter` вызывают исключение `NotImplementedError`, Python не знает, что делать при вызове этих методов. На следующем этапе мы создадим конкретный подкласс, который предоставит эти реализации.
