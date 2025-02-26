# 準備

前のエクササイズでは、データ構造の定義を簡単にする `Structure` クラスを作成しました。たとえば：

```python
class Stock(Structure):
    _fields = ('name','shares','price')
```

これはうまく機能しますが、`__init__()` 関数についてはたくさんのことがとても奇妙です。たとえば、`help(Stock)` を使ってヘルプを求めると、何らかの有用なシグネチャが得られません。また、キーワード引数の渡し方が機能しません。たとえば：

```python
>>> help(Stock)
... 出力を見る...

>>> s = Stock(name='GOOG', shares=100, price=490.1)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: __init__() got an unexpected keyword argument 'price'
>>>
```

このエクササイズでは、この問題に対する別のアプローチを見ていきます。
