# 束縛メソッド

関数呼び出し演算子 `()` によってまだ呼び出されていないメソッドは、「束縛メソッド」と呼ばれます。それは、その元となったインスタンスで動作します。

```python
>>> s = stock.Stock('GOOG', 100, 490.10)
>>> s
<Stock object at 0x590d0>
>>> c = s.cost
>>> c
<bound method Stock.cost of <Stock object at 0x590d0>>
>>> c()
49010.0
>>>
```

束縛メソッドは、しばしば不注意で明確でないエラーの原因になります。たとえば：

```python
>>> s = stock.Stock('GOOG', 100, 490.10)
>>> print('Cost : %0.2f' % s.cost)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: float argument required
>>>
```

または、デバッグが難しい巧妙な動作もあります。

```python
f = open(filename, 'w')
...
f.close     # あっとう！何もしませんでした。`f` はまだ開いたままです。
```

これらの場合の両方で、エラーの原因は、末尾の丸括弧を忘れてしまったことによります。たとえば、`s.cost()` または `f.close()` です。
