# パッケージの作成

以前の実験では、型チェックされた構造体、データの読み取り、テーブルの作成に関連する次のファイルを作成しました。

- `structure.py`
- `validate.py`
- `reader.py`
- `tableformat.py`

あなたのタスクは、これらのすべてのファイルを取り、`structly`と呼ばれるパッケージに移動させることです。そのためには、次の手順に従ってください。

- `structly`と呼ばれるディレクトリを作成する
- 空のファイル`__init__.py`を作成し、`structly`ディレクトリに置く
- `structure.py`、`validate.py`、`reader.py`、および`tableformat.py`の各ファイルを`structly`ディレクトリに移動する
- モジュール間のインポート文を修正する（特に、`structure`モジュールは`validate`に依存している）。

これを行ったら、`stock.py`プログラムを次のように変更して、正しく動作するようにします。

```python
# stock.py

from structly.structure import Structure

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
    from structly.reader import read_csv_as_instances
    from structly.tableformat import create_formatter, print_table
    portfolio = read_csv_as_instances('portfolio.csv', Stock)
    formatter = create_formatter('text')
    print_table(portfolio, ['name','shares','price'], formatter)
```
