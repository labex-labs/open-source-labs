# Регистрация подклассов

Попробуйте следующий эксперимент и наблюдайте:

```python
>>> from structly.tableformat.formats.text import TextTableFormatter
>>> TextTableFormatter.__module__
'structly.tableformat.formats.text'
>>> TextTableFormatter.__module__.split('.')[-1]
'text'
>>>
```

Измените базовый класс `TableFormatter`, добавив словарь и метод `__init_subclass__()`:

```python
class TableFormatter(ABC):
    _formats = { }

    @classmethod
    def __init_subclass__(cls):
        name = cls.__module__.split('.')[-1]
        TableFormatter._formats[name] = cls

    @abstractmethod
    def headings(self, headers):
        pass

    @abstractmethod
    def row(self, rowdata):
        pass
```

Это позволяет родительскому классу отслеживать все свои подклассы. Проверьте это:

```python
>>> from structly.tableformat.formatter import TableFormatter
>>> TableFormatter._formats
{'text': <class'structly.tableformat.formats.text.TextTableFormatter'>,
 'csv': <class'structly.tableformat.formats.csv.CSVTableFormatter'>,
 'html': <class'structly.tableformat.formats.html.HTMLTableFormatter'>}
>>>
```

Измените функцию `create_formatter()`, чтобы искать класс в этом словаре вместо этого:

```python
def create_formatter(name, column_formats=None, upper_headers=False):
    formatter_cls = TableFormatter._formats.get(name)
    if not formatter_cls:
        raise RuntimeError('Unknown format %s' % name)

    if column_formats:
        class formatter_cls(ColumnFormatMixin, formatter_cls):
              formats = column_formats

    if upper_headers:
        class formatter_cls(UpperHeadersMixin, formatter_cls):
            pass

    return formatter_cls()
```

Запустите программу `stock.py`. Убедитесь, что она по-прежнему работает после внесения этих изменений. Просто заметка, что все инструкции импорта по-прежнему там. Вы в основном только немного очистили код и избавились от жестко закодированных имен классов.
