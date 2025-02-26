# 動作中のディスクリプタ

以前、スロット、プロパティ、その他の機能を利用する `Stock` クラスを作成しました。これらの機能はすべて、ディスクリプタプロトコルを使用して実装されています。この簡単な実験を試して、それを動作させてみましょう。

まず、株式オブジェクトを作成し、いくつかの属性を参照してみましょう。

```python
>>> s = Stock('GOOG', 100, 490.10)
>>> s.name
'GOOG'
>>> s.shares
100
>>>
```

次に、これらの属性がクラス辞書にあることに注意してください。

```python
>>> Stock.__dict__.keys()
['sell', '__module__', '__weakref__', 'price', '_price','shares', '_shares',
'__slots__', 'cost', '__repr__', '__doc__', '__init__']
>>>
```

インスタンスでディスクリプタが値を取得および設定する方法を示す次の手順を試してみましょう。

```python
>>> q = Stock.__dict__['shares']
>>> q.__get__(s)
100
>>> q.__set__(s,75)
>>> s.shares
75
>>> q.__set__(s, '75')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "stock.py", line 23, in shares
    raise TypeError('Expected an integer')
TypeError: Expected an integer
>>>
```

`__get__()` と `__set__()` の実行は、インスタンスにアクセスするたびに自動的に行われます。
