# 循環インポート

次のインポート文を `formatter.py` ファイルの先頭に移動してみてください。

```python
# formatter.py

from.formats.text import TextTableFormatter
from.formats.csv import CSVTableFormatter
from.formats.html import HTMLTableFormatter

class TableFormatter(ABC):
    @abstractmethod
    def headings(self, headers):
        pass

    @abstractmethod
    def row(self, rowdata):
        pass

...
```

何も機能しなくなったことに気づきます。`stock.py` プログラムを実行してみて、`TableFormatter` が定義されていないというエラーに気づいてください。インポート文の順序は重要で、好きな場所にインポートを移動することはできません。

インポート文を元の場所に戻しましょう。ああ。
