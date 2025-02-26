# バウンドメソッド

驚くかもしれませんが、メソッド呼び出しは単純な属性に対して使用される仕組みの上に重ねられています。基本的に、メソッドは関数のように呼び出すために必要な丸括弧 () を追加すると実行される属性です。たとえば：

```python
>>> s = Stock('GOOG',100,490.10)
>>> s.cost           # メソッドを参照
<bound method Stock.cost of <__main__.Stock object at 0x409530>>
>>> s.cost()         # メソッドを参照して呼び出す
49010.0

>>> # getattr() を使った同じ操作
>>> getattr(s, 'cost')
<bound method Stock.cost of <__main__.Stock object at 0x409530>>
>>> getattr(s, 'cost')()
49010.0
>>>
```

バウンドメソッドはその元のオブジェクトに付属しています。そのオブジェクトが変更されると、メソッドはその変更を認識します。メソッドの `__self__` 属性を調べることで、元のオブジェクトを確認できます。

```python
>>> c = s.cost
>>> c()
49010.0
>>> s.shares = 75
>>> c()
36757.5
>>> c.__self__
<__main__.Stock object at 0x409530>
>>> c.__func__
<function cost at 0x37cc30>
>>> c.__func__(c.__self__)      # これが c() を呼び出す際の内部処理
36757.5
>>>
```

仕組みを理解しているかどうか確認するために、`sell()` メソッドで試してみましょう：

```python
>>> f = s.sell
>>> f.__func__(f.__self__, 25)     # s.sell(25) と同じ
>>> s.shares
50
>>>
```
