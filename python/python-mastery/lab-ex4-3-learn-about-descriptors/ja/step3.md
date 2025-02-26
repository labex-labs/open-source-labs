# バリデータからディスクリプタへ

前のエクササイズでは、チェックを行うことができる一連のクラスを書きました。たとえば：

```python
>>> PositiveInteger.check(10)
10
>>> PositiveInteger.check('10')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    raise TypeError('Expected %s' % cls.expected_type)
TypeError: expected <class 'int'>
>>> PositiveInteger.check(-10)
```

これを、`Validator` 基底クラスを単純に変更することでディスクリプタに拡張することができます。次のように変更します：

```python
# validate.py

class Validator:
    def __init__(self, name):
        self.name = name

    @classmethod
    def check(cls, value):
        return value

    def __set__(self, instance, value):
        instance.__dict__[self.name] = self.check(value)
```

注：ディスクリプタに `__get__()` メソッドがないことは、Pythonが属性検索の既定の実装を使用することを意味します。これには、提供された名前がインスタンス辞書で使用される名前と一致する必要があります。

他に変更は必要ありません。次に、`Stock` クラスを変更して、バリデータをディスクリプタとして使用するようにしてみましょう：

```python
class Stock:
    name   = String('name')
    shares = PositiveInteger('shares')
    price  = PositiveFloat('price')

    def __init__(self,name,shares,price):
        self.name = name
        self.shares = shares
        self.price = price
```

クラスが以前と同じように機能することがわかります。コードが大幅に少なくなり、すべての望ましいチェックができるようになります：

```python
>>> s = Stock('GOOG', 100, 490.10)
>>> s.name
'GOOG'
>>> s.shares
100
>>> s.shares = 75
>>> s.shares = '75'
... TypeError...
>>> s.shares = -50
... ValueError...
>>>
```

これはかなり素敵です。ディスクリプタにより、`Stock` クラスの実装を大幅に簡略化することができました。これがディスクリプタの本当の力です。ドットに対する低レベルの制御ができ、驚くべきことができるようになります。
