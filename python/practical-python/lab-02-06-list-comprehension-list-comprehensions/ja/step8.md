# 演習2.21: データ照会

さまざまなデータ照会の例を次のように試してみましょう。

まず、100株を超えるすべてのポートフォリオ保有株のリストです。

```python
>>> more100 = [ s for s in portfolio if s['shares'] > 100 ]
>>> more100
[{'price': 83.44, 'name': 'CAT','shares': 150}, {'price': 51.23, 'name': 'MSFT','shares': 200}]
>>>
```

MSFTとIBMの株に関するすべてのポートフォリオ保有株。

```python
>>> msftibm = [ s for s in portfolio if s['name'] in {'MSFT','IBM'} ]
>>> msftibm
[{'price': 91.1, 'name': 'IBM','shares': 50}, {'price': 51.23, 'name': 'MSFT','shares': 200},
  {'price': 65.1, 'name': 'MSFT','shares': 50}, {'price': 70.44, 'name': 'IBM','shares': 100}]
>>>
```

10000ドル以上のコストがかかるすべてのポートフォリオ保有株のリスト。

```python
>>> cost10k = [ s for s in portfolio if s['shares'] * s['price'] > 10000 ]
>>> cost10k
[{'price': 83.44, 'name': 'CAT','shares': 150}, {'price': 51.23, 'name': 'MSFT','shares': 200}]
>>>
```
