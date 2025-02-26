# 可変整数

Python の整数は通常不変です。ただし、可変な整数オブジェクトを作成したいとしましょう。まずはこのようなクラスを作成します。

```python
# mutint.py

class MutInt:
    __slots__ = ['value']

    def __init__(self, value):
        self.value = value
```

試してみましょう。

```python
>>> a = MutInt(3)
>>> a
<__main__.MutInt object at 0x10e79d408>
>>> a.value
3
>>> a.value = 42
>>> a.value
42
>>> a + 10
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unsupported operand type(s) for +: 'MutInt' and 'int'
>>>
```

これはとても面白いですが、この新しい `MutInt` オブジェクトと何もうまく機能しません。表示がひどく、数学演算子はどれも機能せず、基本的にはあまり役に立ちません。ただし、その値は可変であるという事実を除けば、それは持っています。
