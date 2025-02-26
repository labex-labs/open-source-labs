# モジュール分割

`structly/tableformat.py` ファイルには、さまざまな形式でテーブルを作成するコードが含まれています。具体的には：

- `TableFormatter` 基底クラス。
- `TextTableFormatter` クラス。
- `CSVTableFormatter` クラス。
- `HTMLTableFormatter` クラス。

これらのクラスをすべて1つの `.py` ファイルに収める代わりに、各具体的なフォーマッタをそれぞれ独自のファイルに移動する方が理にかなっているかもしれません。これを行うには、`tableformat.py` ファイルを分割します。次の手順に従ってください。

まず、`structly/__pycache__` ディレクトリを削除します。

    % cd structly
    % rm -rf __pycache__

次に、`structly/tableformat` ディレクトリを作成します。このディレクトリ名は、置き換えるモジュール（`tableformat.py`）とまったく同じ名前でなければなりません。

```bash
mkdir tableformat
```

元の `tableformat.py` ファイルを新しい `tableformat` ディレクトリに移動し、`formatter.py` にリネームします。

```bash
mv tableformat.py tableformat/formatter.py
```

`tableformat` ディレクトリ内で、`tableformat.py` のコードを次のファイルとディレクトリに分割します。

- `formatter.py` - `TableFormatter` 基底クラス、ミックスイン、およびさまざまな関数を含む。
- `formats/text.py` - `TextTableFormatter` クラスを含む。
- `formats/csv.py` - `CSVTableFormatter` クラスを含む。
- `formats/html.py` - `HTMLTableFormatter` クラスを含む。

`tableformat/` と `tableformat/formats` ディレクトリに `__init__.py` ファイルを追加します。`tableformat/__init__.py` は、元の `tableformat.py` ファイルがエクスポートしたものと同じシンボルをエクスポートするようにします。

これらの変更をすべて行った後、次のようなパッケージ構造になるはずです。

    structly/
          __init__.py
          validate.py
          reader.py
          structure.py
          tableformat/
               __init__.py
               formatter.py
               formats/
                   __init__.py
                   text.py
                   csv.py
                   html.py

ユーザにとっては、すべてが以前とまったく同じように機能するはずです。たとえば、以前の `stock.py` ファイルは機能します。

```python
# stock.py

from structly import *

class Stock(Structure):
    name = String()
    shares = PositiveInteger()
    price = PositiveFloat()

    @property
    def cost(self):
        return self.shares * self.price

    def sell(self, nshares):
        self.shares -= nshares

if __name__ == '__main__':
    portfolio = read_csv_as_instances('portfolio.csv', Stock)
    formatter = create_formatter('text')
    print_table(portfolio, ['name','shares','price'], formatter)
```
