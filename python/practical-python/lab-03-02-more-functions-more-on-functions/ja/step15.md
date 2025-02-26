# 演習3.5: 型変換の実行

`/home/labex/project/fileparse_3.5.py` ディレクトリ内の `parse_csv()` 関数を修正して、返されるデータに対して任意で型変換を適用できるようにしましょう。たとえば：

```python
>>> portfolio = parse_csv('/home/labex/project/portfolio.csv', types=[str, int, float])
>>> portfolio
[{'name': 'AA','shares': 100, 'price': 32.2}, {'name': 'IBM','shares': 50, 'price': 91.1}, {'name': 'CAT','shares': 150, 'price': 83.44}, {'name': 'MSFT','shares': 200, 'price': 51.23}, {'name': 'GE','shares': 95, 'price': 40.37}, {'name': 'MSFT','shares': 50, 'price': 65.1}, {'name': 'IBM','shares': 100, 'price': 70.44}]

>>> shares_held = parse_csv('/home/labex/project/portfolio.csv', select=['name','shares'], types=[str, int])
>>> shares_held
[{'name': 'AA','shares': 100}, {'name': 'IBM','shares': 50}, {'name': 'CAT','shares': 150}, {'name': 'MSFT','shares': 200}, {'name': 'GE','shares': 95}, {'name': 'MSFT','shares': 50}, {'name': 'IBM','shares': 100}]
>>>
```

演習2.24で既にこれを検討しています。コードの次のフラグメントをソリューションに挿入する必要があります。

```python
...
if types:
    row = [func(val) for func, val in zip(types, row) ]
...
```
