# 継承を通じたデコレータの適用

クラスデコレータ自体を指定する必要があるのは厄介です。次の `__init_subclass__()` メソッドを使って `Structure` クラスを変更します。

```python
# structure.py

class Structure:
 ...
    @classmethod
    def __init_subclass__(cls):
        validate_attributes(cls)
```

この変更を行ったら、デコレータを完全に削除して、継承のみに依存できるようになります。これは継承といくつかの隠れた魔法の組み合わせです！

```python
# stock.py

from structure import Structure
from validate import String, PositiveInteger, PositiveFloat

class Stock(Structure):
    name = String()
    shares = PositiveInteger()
    price = PositiveFloat()

    @property
    def cost(self):
        return self.shares * self.price

    def sell(self, nshares):
        self.shares -= nshares
```

今や、コードは本当に上手くいってきています。実際、ほとんど普通に見えます。これをさらに進めましょう。
