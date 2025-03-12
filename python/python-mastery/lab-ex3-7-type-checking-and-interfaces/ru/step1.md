# Добавление проверки типов в функцию print_table()

На этом этапе мы улучшим функцию `print_table()` в файле `tableformat.py`. Мы добавим проверку, является ли параметр `formatter` допустимым экземпляром `TableFormatter`. Почему это необходимо? Проверка типов - это своего рода страховка для вашего кода. Она помогает убедиться, что данные, с которыми вы работаете, имеют правильный тип, что может предотвратить множество трудноуловимых ошибок.

## Понимание проверки типов в Python

Проверка типов - это очень полезная техника в программировании. Она позволяет выявлять ошибки на ранних этапах разработки. В Python мы часто работаем с разными типами объектов, и иногда мы ожидаем, что в функцию будет передан объект определенного типа. Чтобы проверить, является ли объект определенного типа или его подклассом, мы можем использовать функцию `isinstance()`. Например, если у вас есть функция, которая ожидает список, вы можете использовать `isinstance()`, чтобы убедиться, что входные данные действительно являются списком.

## Изменение функции print_table()

Сначала откройте файл `tableformat.py` в вашем редакторе кода. Прокрутите файл до конца, и вы найдете функцию `print_table()`. Вот как она выглядит изначально:

```python
def print_table(data, columns, formatter):
    '''
    Print a table showing selected columns from a data source
    using the given formatter.
    '''
    formatter.headings(columns)
    for item in data:
        rowdata = [str(getattr(item, col)) for col in columns]
        formatter.row(rowdata)
```

Эта функция принимает некоторые данные, список столбцов и форматер. Затем она использует форматер для вывода таблицы. Но в данный момент она не проверяет, является ли форматер правильного типа.

Давайте изменим ее, чтобы добавить проверку типов. Мы будем использовать функцию `isinstance()`, чтобы проверить, является ли параметр `formatter` экземпляром `TableFormatter`. Если это не так, мы вызовем исключение `TypeError` с четким сообщением. Вот модифицированный код:

```python
def print_table(data, columns, formatter):
    '''
    Print a table showing selected columns from a data source
    using the given formatter.
    '''
    if not isinstance(formatter, TableFormatter):
        raise TypeError("Expected a TableFormatter")

    formatter.headings(columns)
    for item in data:
        rowdata = [str(getattr(item, col)) for col in columns]
        formatter.row(rowdata)
```

## Тестирование реализации проверки типов

Теперь, когда мы добавили проверку типов, нам нужно убедиться, что она работает. Давайте создадим новый Python-файл с именем `test_tableformat.py`. Вот код, который вы должны поместить в него:

```python
import stock
import reader
import tableformat

# Read portfolio data
portfolio = reader.read_csv_as_instances('portfolio.csv', stock.Stock)

# Define a formatter that doesn't inherit from TableFormatter
class MyFormatter:
    def headings(self, headers):
        pass
    def row(self, rowdata):
        pass

# Try to use the non-compliant formatter
try:
    tableformat.print_table(portfolio, ['name', 'shares', 'price'], MyFormatter())
    print("Test failed - type checking not implemented")
except TypeError as e:
    print(f"Test passed - caught error: {e}")
```

В этом коде мы сначала считываем данные о портфеле. Затем мы определяем новый класс форматера с именем `MyFormatter`, который не наследуется от `TableFormatter`. Мы пытаемся использовать этот несоответствующий форматер в функции `print_table()`. Если наша проверка типов работает, она должна вызвать исключение `TypeError`.

Чтобы запустить тест, откройте терминал и перейдите в каталог, где находится файл `test_tableformat.py`. Затем выполните следующую команду:

```bash
python test_tableformat.py
```

Если все работает правильно, вы должны увидеть вывод, похожий на следующий:

```
Test passed - caught error: Expected a TableFormatter
```

Этот вывод подтверждает, что наша проверка типов работает как ожидалось. Теперь функция `print_table()` будет принимать только форматеры, которые являются экземплярами `TableFormatter` или его подклассов.
