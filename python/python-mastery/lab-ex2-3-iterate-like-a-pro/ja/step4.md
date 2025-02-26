# zip() 関数の使用

`zip()` 関数は、最も一般的にはデータをペアにするために使用されます。たとえば、`headers` 変数を作成したことを思い出してください：

```python
>>> headers
['name','shares', 'price']
>>>
```

これは、他の行データと組み合わせるのに便利かもしれません：

```python
>>> row = rows[0]
>>> row
['AA', '100', '32.20']
>>> for col, val in zip(headers, row):
        print(col, val)

name AA
shares 100
price 32.20
>>>
```

あるいは、辞書を作成するために使用できるかもしれません：

```python
>>> dict(zip(headers, row))
{'name': 'AA','shares': '100', 'price': '32.20'}
>>>
```

あるいは、辞書のシーケンスを作成するかもしれません：

```python
>>> for row in rows:
        record = dict(zip(headers, row))
        print(record)

{'name': 'AA','shares': '100', 'price': '32.20'}
{'name': 'IBM','shares': '50', 'price': '91.10'}
{'name': 'CAT','shares': '150', 'price': '83.44'}
{'name': 'MSFT','shares': '200', 'price': '51.23'}
{'name': 'GE','shares': '95', 'price': '40.37'}
{'name': 'MSFT','shares': '50', 'price': '65.10'}
{'name': 'IBM','shares': '100', 'price': '70.44'}
>>>
```
