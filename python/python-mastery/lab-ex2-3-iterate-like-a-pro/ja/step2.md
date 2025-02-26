# 基本的な反復処理と展開

`for` 文は、任意のデータのシーケンスを反復処理します。たとえば：

```python
>>> for row in rows:
        print(row)

['AA', '100', '32.20']
['IBM', '50', '91.10']
['CAT', '150', '83.44']
['MSFT', '200', '51.23']
['GE', '95', '40.37']
['MSFT', '50', '65.10']
['IBM', '100', '70.44']
>>>
```

必要に応じて、値を個別の変数に展開します：

```python
>>> for name, shares, price in rows:
        print(name, shares, price)

AA 100 32.20
IBM 50 91.10
CAT 150 83.44
MSFT 200 51.23
GE 95 40.37
MSFT 50 65.10
IBM 100 70.44
>>>
```

1つ以上の値を気にしない場合、捨てる変数として `_` または `__` を使用するのはやや一般的です。たとえば：

```python
>>> for name, _, price in rows:
        print(name, price)

AA 32.20
IBM 91.10
CAT 83.44
MSFT 51.23
GE 40.37
MSFT 65.10
IBM 70.44
>>>
```

展開される値の数がわからない場合、ワイルドカードとして `*` を使用できます。データを名前でグループ化するこの実験を試してみてください：

```python
>>> from collections import defaultdict
>>> byname = defaultdict(list)
>>> for name, *data in rows:
        byname[name].append(data)

>>> byname['IBM']
[['50', '91.10'], ['100', '70.44']]
>>> byname['CAT']
[['150', '83.44']]
>>> for shares, price in byname['IBM']:
        print(shares, price)

50 91.10
100 70.44
>>>
```
