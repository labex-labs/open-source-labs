# コード生成器としてのクロージャ

演習4.3では、オブジェクト属性の型チェックを可能にするディスクリプタクラスのコレクションを開発しました。たとえば：

```python

class Stock:
    name = String()
    shares = Integer()
    price = Float()
```

このようなことは、クロージャを使っても実装できます。`typedproperty.py` というファイルを定義し、次のコードを入れましょう：

```python
# typedproperty.py

def typedproperty(name, expected_type):
    private_name = '_' + name

    @property
    def value(self):
        return getattr(self, private_name)

    @value.setter
    def value(self, val):
        if not isinstance(val, expected_type):
            raise TypeError(f'Expected {expected_type}')
        setattr(self, private_name, val)

    return value
```

これはかなり奇妙に見えますが、この関数は実際にコードを生成しています。これを次のようなクラス定義で使います：

```python
from typedproperty import typedproperty

class Stock:
    name = typedproperty('name', str)
    shares = typedproperty('shares', int)
    price = typedproperty('price', float)

    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price
```

このクラスが、ディスクリプタコードと同じように型チェックを行うことを確認してください。

`String()`, `Integer()`, および `Float()` 関数を `typedproperty.py` ファイルに追加して、次のコードを書けるようにしましょう：

```python
from typedproperty import String, Integer, Float

class Stock:
    name = String('name')
    shares = Integer('shares')
    price = Float('price')
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price
```
