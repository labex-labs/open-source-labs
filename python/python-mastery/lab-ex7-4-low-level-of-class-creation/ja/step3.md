# 多数のクラスの作成

`type()` コンストラクタを直接使用すると有利な場合もあります。次のコードを見てみましょう。

```python
# validate.py
...

class Typed(Validator):
    expected_type = object
    @classmethod
    def check(cls, value):
        if not isinstance(value, cls.expected_type):
            raise TypeError(f'expected {cls.expected_type}')
        super().check(value)

class Integer(Typed):
    expected_type = int

class Float(Typed):
    expected_type = float

class String(Typed):
    expected_type = str
...
```

ああ、最後の部分は面倒くさく繰り返していますね。これを、次のように望ましい型クラスのテーブルを使って変更しましょう。

```python
# validate.py
...

_typed_classes = [
    ('Integer', int),
    ('Float', float),
    ('String', str) ]

globals().update((name, type(name, (Typed,), {'expected_type':ty}))
                 for name, ty in _typed_classes)
```

これで、もっと多くの型クラスが必要な場合、ただテーブルに追加するだけです。

```python
_typed_classes = [
    ('Integer', int),
    ('Float', float),
    ('Complex', complex),
    ('Decimal', decimal.Decimal),
    ('List', list),
    ('Bool', bool),
    ('String', str) ]
```

認めてしまえ、これはかなりかっこいいし、キーボード操作をたくさん省けます。
