# インスタンス データ

各インスタンスには独自のローカル データがあります。

```python
>>> a.x
2
>>> b.x
10
```

このデータは `__init__()` によって初期化されます。

```python
class Player:
    def __init__(self, x, y):
        # `self` に格納される任意の値はインスタンス データです
        self.x = x
        self.y = y
        self.health = 100
```

格納される属性の総数や型に制限はありません。
