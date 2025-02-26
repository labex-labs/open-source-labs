# 比較

1つの問題は、比較がまだ機能しないことです。たとえば：

```python
>>> a = MutInt(3)
>>> b = MutInt(3)
>>> a == b
False
>>> a == 3
False
>>>
```

これを修正するには、`__eq__()` メソッドを追加します。さらに、`__lt__()`、`__le__()`、`__gt__()`、`__ge__()` などのメソッドを使用して、他の比較を実装することができます。たとえば：

```python
class MutInt:
    __slots__ = ['value']

    def __init__(self, value):
        self.value = value

 ...
    def __eq__(self, other):
        if isinstance(other, MutInt):
            return self.value == other.value
        elif isinstance(other, int):
            return self.value == other
        else:
            return NotImplemented

    def __lt__(self, other):
        if isinstance(other, MutInt):
            return self.value < other.value
        elif isinstance(other, int):
            return self.value < other
        else:
            return NotImplemented
```

試してみましょう。

```python
>>> a = MutInt(3)
>>> b = MutInt(3)
>>> a == b
True
>>> c = MutInt(4)
>>> a < c
True
>>> a <= c
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: '<=' not supported between instances of 'MutInt' and 'MutInt'
>>>
```

`<=` 演算子が失敗する原因は、`__le__()` メソッドが提供されていないことです。個別にコードを記述することもできますが、簡単な方法は `@total_ordering` デコレータを使用することです。

```python
from functools import total_ordering

@total_ordering
class MutInt:
    __slots__ = ['value']

    def __init__(self, value):
        self.value = value

 ...

    def __eq__(self, other):
        if isinstance(other, MutInt):
            return self.value == other.value
        elif isinstance(other, int):
            return self.value == other
        else:
            return NotImplemented

    def __lt__(self, other):
        if isinstance(other, MutInt):
            return self.value < other.value
        elif isinstance(other, int):
            return self.value < other
        else:
            return NotImplemented
```

`@total_ordering` は、等価演算子と他の関係の1つを最小限提供する限り、欠落している比較メソッドを自動的に埋めてくれます。
