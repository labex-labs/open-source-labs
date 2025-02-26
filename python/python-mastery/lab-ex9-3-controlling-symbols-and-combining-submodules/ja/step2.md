# エクスポートされるシンボルの制御

`structly` パッケージ内のすべてのサブモジュールを変更して、選択されたシンボルをエクスポートする `__all__` 変数を明示的に定義します。具体的には：

- `structure.py` は `Structure` をエクスポートする必要があります。
- `reader.py` はすべての `read_csv_as_*()` 関数をエクスポートする必要があります。
- `tableformat.py` は `create_formatter()` と `print_table()` をエクスポートします。

次に、`__init__.py` ファイルで、すべてのサブモジュールを次のように統一します。

```python
# structly/__init__.py

from.structure import *
from.reader import *
from.tableformat import *
```

これを行った後、単一の論理モジュールからすべてをインポートできるようになります。

```python
# stock.py

from structly import Structure

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
    from structly import read_csv_as_instances, create_formatter, print_table
    portfolio = read_csv_as_instances('portfolio.csv', Stock)
    formatter = create_formatter('text')
    print_table(portfolio, ['name','shares','price'], formatter)
```
