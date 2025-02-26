# 動的インポート

これで最後のフロンティアに向かう準備が整いました。次のインポート文をすべて削除します。

```python
# formatter.py
...

from.formats.text import TextTableFormatter     # DELETE
from.formats.csv import CSVTableFormatter       # DELETE
from.formats.html import HTMLTableFormatter     # DELETE
...
```

再度、`stock.py` コードを実行します。エラーが発生して失敗するはずです。テキストフォーマッターについて何も知りません。`create_formatter()` にこの小さなコード断片を追加することで修正します。

```python
def create_formatter(name, column_formats=None, upper_headers=False):
    if name not in TableFormatter._formats:
        __import__(f'{__package__}.formats.{name}')
  ...
```

このコードは、名前に関して何も知らない場合に、フォーマッターモジュールの動的インポートを試みます。インポートだけで（うまくいけば）クラスが `_formats` 辞書に登録され、すべてがうまく機能します。魔法です！

`stock.py` コードを実行して、その後機能することを確認してみてください。
