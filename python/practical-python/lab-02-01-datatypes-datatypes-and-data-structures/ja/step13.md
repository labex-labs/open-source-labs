# 演習 2.3: 追加の辞書操作

辞書をリストに変換すると、そのすべてのキーが得られます。

```python
>>> list(d)
['name','shares', 'price', 'date', 'account']
>>>
```

同様に、辞書に対して`for`文を使って反復処理を行うと、キーが得られます。

```python
>>> for k in d:
        print('k =', k)

k = name
k = shares
k = price
k = date
k = account
>>>
```

同時に検索を行うこのバリアントを試してみましょう。

```python
>>> for k in d:
        print(k, '=', d[k])

name = AA
shares = 75
price = 32.2
date = (6, 11, 2007)
account = 12345
>>>
```

また、`keys()`メソッドを使ってすべてのキーを取得することもできます。

```python
>>> keys = d.keys()
>>> keys
dict_keys(['name','shares', 'price', 'date', 'account'])
>>>
```

`keys()`は少し異なり、特殊な`dict_keys`オブジェクトを返します。

これは元の辞書のオーバーレイで、辞書が変更されても常に現在のキーを返します。たとえば、これを試してみましょう。

```python
>>> del d['account']
>>> keys
dict_keys(['name','shares', 'price', 'date'])
>>>
```

`'account'`が`keys`から消えたことに注意してください。再度`d.keys()`を呼び出さなくてもです。

キーと値を一緒に扱うよりエレガントな方法は、`items()`メソッドを使うことです。これは`(キー, 値)`のタプルを返します。

```python
>>> items = d.items()
>>> items
dict_items([('name', 'AA'), ('shares', 75), ('price', 32.2), ('date', (6, 11, 2007))])
>>> for k, v in d.items():
        print(k, '=', v)

name = AA
shares = 75
price = 32.2
date = (6, 11, 2007)
>>>
```

`items`のようなタプルがある場合、`dict()`関数を使って辞書を作成することができます。試してみましょう。

```python
>>> items
dict_items([('name', 'AA'), ('shares', 75), ('price', 32.2), ('date', (6, 11, 2007))])
>>> d = dict(items)
>>> d
{'name': 'AA','shares': 75, 'price':32.2, 'date': (6, 11, 2007)}
>>>
```
