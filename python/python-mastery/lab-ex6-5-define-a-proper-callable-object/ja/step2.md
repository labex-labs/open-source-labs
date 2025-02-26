# コール可能オブジェクトの作成

`validate.py` ファイルで、次のようなクラスを作成します。

```python
# validate.py
...

class ValidatedFunction:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        print('Calling', self.func)
        result = self.func(*args, **kwargs)
        return result
```

関数に適用してクラスをテストします。

```python
>>> def add(x, y):
        return x + y

>>> add = ValidatedFunction(add)
>>> add(2, 3)
Calling <function add at 0x1014df598>
5
>>>
```
