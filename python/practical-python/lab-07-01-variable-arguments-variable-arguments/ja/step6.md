# 演習 7.2：引数としてタプルと辞書を渡す

あるファイルからデータを読み取り、次のようなタプルを取得したとしましょう。

```python
>>> data = ('GOOG', 100, 490.1)
>>>
```

今、このデータから `Stock` オブジェクトを作成したいとします。`data` を直接渡そうとすると、うまくいきません。

```python
>>> from stock import Stock
>>> s = Stock(data)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: Stock.__init__() missing 2 required positional arguments:'shares' and 'price'
>>>
```

代わりに `*data` を使うことで簡単に修正できます。試してみてください。

```python
>>> s = Stock(*data)
>>> s
Stock('GOOG', 100, 490.1)
>>>
```

辞書がある場合は、代わりに `**` を使うことができます。たとえば：

```python
>>> data = { 'name': 'GOOG','shares': 100, 'price': 490.1 }
>>> s = Stock(**data)
Stock('GOOG', 100, 490.1)
>>>
```
