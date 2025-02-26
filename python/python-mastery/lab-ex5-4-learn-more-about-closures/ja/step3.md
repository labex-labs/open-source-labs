# チャレンジ：名前の削除

`typedproperty.py` のコードを変更して、属性名が不要になるようにしましょう：

```python
from typedproperty import String, Integer, Float

class Stock:
    name = String()
    shares = Integer()
    price = Float()
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price
```

ヒント：これを行うには、ディスクリプタがクラス定義に配置されたときに呼び出されるディスクリプタオブジェクトの `__set_name__()` メソッドを思い出してください。
