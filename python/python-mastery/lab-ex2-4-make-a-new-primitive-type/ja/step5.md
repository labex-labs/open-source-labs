# 変換

あなたの新しいプリミティブ型はほぼ完成しています。いくつかの一般的な変換を行う機能を与えたい場合があります。たとえば：

```python
>>> a = MutInt(3)
>>> int(a)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: int() argument must be a string, a bytes-like object or a number, not 'MutInt'
>>> float(a)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: float() argument must be a string, a bytes-like object or a number, not 'MutInt'
>>>
```

これを修正するには、クラスに `__int__()` と `__float__()` メソッドを与えます。

```python
from functools import total_ordering

@total_ordering
class MutInt:
    __slots__ = ['value']

    def __init__(self, value):
        self.value = value

 ...

    def __int__(self):
        return self.value

    def __float__(self):
        return float(self.value)
```

これで、適切に変換できるようになります。

```python
>>> a = MutInt(3)
>>> int(a)
3
>>> float(a)
3.0
>>>
```

一般的なルールとして、Pythonはデータを自動的に変換しません。したがって、クラスに `__int__()` メソッドを与えたとしても、整数が期待されるすべての状況で `MutInt` が機能するとは限りません。たとえば、インデックス付け：

```python
>>> names = ['Dave', 'Guido', 'Paula', 'Thomas', 'Lewis']
>>> a = MutInt(1)
>>> names[a]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: list indices must be integers or slices, not MutInt
>>>
```

これは、整数を生成する `__index__()` メソッドを `MutInt` に与えることで修正できます。クラスを次のように変更します。

```python
from functools import total_ordering

@total_ordering
class MutInt:
    __slots__ = ['value']

    def __init__(self, value):
        self.value = value

 ...

    def __int__(self):
        return self.value

    __index__ = __int__     # インデックス付けを機能させる
```

**考察**

新しいプリミティブデータ型を作成することは、実際にはPythonで最も複雑なプログラミングタスクの1つです。たくさんの端数ケースや低レベルの問題があり、特にあなたの型が他のPython型とどのように相互作用するかに関して心配する必要があります。おそらく忘れてはいけない重要なことは、基礎となるプロトコルを知っていれば、オブジェクトがPythonの他の部分とどのように相互作用するかのほとんどすべての側面をカスタマイズできるということです。これを行う場合、作成しようとしているものに似た既存のコードを見ることがおすすめです。
