# オブジェクトを表すためのより良い出力

すべてのPythonオブジェクトは2つの文字列表現を持っています。最初の表現は、`str()`を通じた文字列変換によって作成されます（これは`print`によって呼び出されます）。文字列表現は通常、人間にとって見やすくフォーマットされたオブジェクトのバージョンです。2番目の表現は、`repr()`によって作成されるオブジェクトのコード表現です（または、対話型シェルで値を表示することによって簡単に作成されます）。コード表現は通常、オブジェクトを取得するために入力する必要のあるコードを表示します。日付を使用した例を以下に示します。

```python
>>> from datetime import date
>>> d = date(2008, 7, 5)
>>> print(d)              # str()を使用
2008-07-05
>>> d    # repr()を使用
datetime.date(2008, 7, 5)
>>>
```

出力において`repr()`文字列取得するためのいくつかの技法があります。

```python
>>> print('The date is', repr(d))
The date is datetime.date(2008, 7, 5)
>>> print(f'The date is {d!r}')
The date is datetime.date(2008, 7, 5)
>>> print('The date is %r' % d)
The date is datetime.date(2008, 7, 5)
>>>
```

作成した`Stock`オブジェクトを変更して、`__repr__()`メソッドがより有用な出力を生成するようにします。たとえば：

```python
>>> goog = Stock('GOOG', 100, 490.10)
>>> goog
Stock('GOOG', 100, 490.1)
>>>
```

株式のポートフォリオを読み込み、これらの変更を行った後に結果のリストを表示したときに何が起こるかを確認します。たとえば：

```python
>>> import stock, reader
>>> portfolio = reader.read_csv_as_instances('portfolio.csv', stock.Stock)
>>> portfolio
[Stock('AA', 100, 32.2), Stock('IBM', 50, 91.1), Stock('CAT', 150, 83.44), Stock('MSFT', 200, 51.23),
 Stock('GE', 95, 40.37), Stock('MSFT', 50, 65.1), Stock('IBM', 100, 70.44)]
>>>
```
