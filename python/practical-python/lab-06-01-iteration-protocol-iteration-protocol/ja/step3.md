# 反復処理のサポート

自分自身のオブジェクトに反復処理を追加したい場合、反復処理について知っておくと便利です。たとえば、カスタムコンテナを作成する場合です。

```python
class Portfolio:
    def __init__(self):
        self.holdings = []

    def __iter__(self):
        return self.holdings.__iter__()
  ...

port = Portfolio()
for s in port:
  ...
```
