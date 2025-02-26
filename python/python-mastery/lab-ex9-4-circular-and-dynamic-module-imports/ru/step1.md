# Подготовка

В предыдущем упражнении вы разделили файл `tableformat.py` на подмодули. Последняя часть получившегося файла `tableformat/formatter.py` превратилась в беспорядок импортов.

```python
# tableformat.py
...

class TableFormatter(ABC):
    @abstractmethod
    def headings(self, headers):
        pass

    @abstractmethod
    def row(self, rowdata):
        pass

from.formats.text import TextTableFormatter
from.formats.csv import CSVTableFormatter
from.formats.html import HTMLTableFormatter

...

def create_formatter(name, column_formats=None, upper_headers=False):
    if name == 'text':
        formatter_cls = TextTableFormatter
    elif name == 'csv':
        formatter_cls = CSVTableFormatter
    elif name == 'html':
        formatter_cls = HTMLTableFormatter
    else:
        raise RuntimeError('Unknown format %s' % name)

    if column_formats:
        class formatter_cls(ColumnFormatMixin, formatter_cls):
              formats = column_formats

    if upper_headers:
        class formatter_cls(UpperHeadersMixin, formatter_cls):
            pass

    return formatter_cls()
```

Импорты в середине файла необходимы, потому что функция `create_formatter()` нуждается в них, чтобы найти соответствующие классы. По правде говоря, вся эта конструкция является беспорядком.
