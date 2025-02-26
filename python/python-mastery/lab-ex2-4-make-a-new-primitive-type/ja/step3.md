# 数学演算子

適切なメソッドを実装することで、オブジェクトを様々な数学演算子と使うことができます。ただし、他のデータ型を認識し、適切な変換コードを実装するのはあなたの責任です。`MutInt` クラスに `__add__()` メソッドを次のように与えて修正します。

```python
class MutInt:
    __slots__ = ['value']

    def __init__(self, value):
        self.value = value

  ...

    def __add__(self, other):
        if isinstance(other, MutInt):
            return MutInt(self.value + other.value)
        elif isinstance(other, int):
            return MutInt(self.value + other)
        else:
            return NotImplemented
```

この変更により、整数と可変整数の両方を加算できるはずです。結果は `MutInt` インスタンスです。他の種類の数値を加算するとエラーになります。

```python
>>> a = MutInt(3)
>>> b = a + 10
>>> b
MutInt(13)
>>> b.value = 23
>>> c = a + b
>>> c
MutInt(26)
>>> a + 3.5
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unsupported operand type(s) for +: 'MutInt' and 'float'
>>>
```

コードの1つの問題は、演算子の順序を逆にした場合に機能しないことです。考えてみましょう。

```python
>>> a + 10
MutInt(13)
>>> 10 + a
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unsupported operand type(s) for +: 'int' and 'MutInt'
>>>
```

これは、`int` 型が `MutInt` を知らないために混乱しているため起こっています。これは、`__radd__()` メソッドを追加することで修正できます。このメソッドは、`__add__()` を最初に呼び出した試みが提供されたオブジェクトで機能しなかった場合に呼び出されます。

```python
class MutInt:
    __slots__ = ['value']

    def __init__(self, value):
        self.value = value

  ...

    def __add__(self, other):
        if isinstance(other, MutInt):
            return MutInt(self.value + other.value)
        elif isinstance(other, int):
            return MutInt(self.value + other)
        else:
            return NotImplemented

    __radd__ = __add__    # 演算子の順序を逆にした場合
```

この変更により、加算が機能するはずです。

```python
>>> a = MutInt(3)
>>> a + 10
MutInt(13)
>>> 10 + a
MutInt(13)
>>>
```

私たちの整数は可変であるため、`__iadd__()` メソッドを実装することで、インプレース加算更新演算子 `+=` を認識させることもできます。

```python
class MutInt:
    __slots__ = ['value']

    def __init__(self, value):
        self.value = value

  ...

    def __iadd__(self, other):
        if isinstance(other, MutInt):
            self.value += other.value
            return self
        elif isinstance(other, int):
            self.value += other
            return self
        else:
            return NotImplemented
```

これにより、次のような面白い使い方が可能になります。

```python
>>> a = MutInt(3)
>>> b = a
>>> a += 10
>>> a
MutInt(13)
>>> b                 # bも変更されることに注意
MutInt(13)
>>>
```

`b` も変更されるのは少し奇妙に見えるかもしれませんが、Pythonの組み込みオブジェクトにはこのような微妙な機能があります。たとえば：

```python
>>> a = [1,2,3]
>>> b = a
>>> a += [4,5]
>>> a
[1, 2, 3, 4, 5]
>>> b
[1, 2, 3, 4, 5]

>>> c = (1,2,3)
>>> d = c
>>> c += (4,5)
>>> c
(1, 2, 3, 4, 5)
>>> d                  # リストとの違いを説明
(1, 2, 3)
>>>
```
