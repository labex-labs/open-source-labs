# 準備

前のエクササイズでは、`tableformat.py` ファイルをサブモジュールに分割しました。結果として得られた `tableformat/formatter.py` ファイルの最後の部分は、インポートの混乱になっています。

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

ファイルの途中のインポートは必要です。なぜなら、`create_formatter()` 関数が適切なクラスを見つけるために必要だからです。実際、全体が混乱しています。
