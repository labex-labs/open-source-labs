# 準備

パッケージには、1つ潜在的に厄介な点があります。それは、インポート文を複雑にすることです。たとえば、`stock.py` プログラムでは、次のようなインポート文があります。

```python
from structly.structure import Structure
from structly.reader import read_csv_as_instances
from structly.tableformat import create_formatter, print_table
```

パッケージが統一された全体として使用されることを想定している場合、すべてを単一のトップレベルパッケージに統合する方が、もっと健全（かつ簡単）かもしれません。それでは、それを行いましょう。
