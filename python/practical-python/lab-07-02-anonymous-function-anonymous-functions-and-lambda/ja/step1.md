# 再訪：リストのソート

リストは _in-place_ でソートできます。`sort` メソッドを使用します。

```python
s = [10,1,7,3]
s.sort() # s = [1,3,7,10]
```

逆順でソートすることもできます。

```python
s = [10,1,7,3]
s.sort(reverse=True) # s = [10,7,3,1]
```

これは十分にシンプルに見えます。しかし、辞書のリストをどのようにソートするのでしょうか。

```python
[{'name': 'AA', 'price': 32.2,'shares': 100},
{'name': 'IBM', 'price': 91.1,'shares': 50},
{'name': 'CAT', 'price': 83.44,'shares': 150},
{'name': 'MSFT', 'price': 51.23,'shares': 200},
{'name': 'GE', 'price': 40.37,'shares': 95},
{'name': 'MSFT', 'price': 65.1,'shares': 50},
{'name': 'IBM', 'price': 70.44,'shares': 100}]
```

どの基準でですか？

ソートをガイドするには、_key 関数_ を使用します。_key 関数_ は、辞書を受け取り、ソートに使用する対象の値を返す関数です。

```python
portfolio = [
    {'name': 'AA', 'price': 32.2,'shares': 100},
    {'name': 'IBM', 'price': 91.1,'shares': 50},
    {'name': 'CAT', 'price': 83.44,'shares': 150},
    {'name': 'MSFT', 'price': 51.23,'shares': 200},
    {'name': 'GE', 'price': 40.37,'shares': 95},
    {'name': 'MSFT', 'price': 65.1,'shares': 50},
    {'name': 'IBM', 'price': 70.44,'shares': 100}
]

def stock_name(s):
    return s['name']

portfolio.sort(key=stock_name)
```

結果は次の通りです。

```python
# `name` キーによる辞書のソート方法を確認する
[
  {'name': 'AA', 'price': 32.2,'shares': 100},
  {'name': 'CAT', 'price': 83.44,'shares': 150},
  {'name': 'GE', 'price': 40.37,'shares': 95},
  {'name': 'IBM', 'price': 91.1,'shares': 50},
  {'name': 'IBM', 'price': 70.44,'shares': 100},
  {'name': 'MSFT', 'price': 51.23,'shares': 200},
  {'name': 'MSFT', 'price': 65.1,'shares': 50}
]
```
