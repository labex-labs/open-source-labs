# 内包表記

リスト、セット、辞書の内包表記は、データを操作するための便利なツールになります。たとえば、次の操作を試してみてください。

```python
>>> # 100株以上の保有株をすべて見つける
>>> [s for s in portfolio if s['shares'] > 100]
[{'name': 'CAT','shares': 150, 'price': 83.44},
 {'name': 'MSFT','shares': 200, 'price': 51.23}]

>>> # 総コストを計算する (株数 * 価格)
>>> sum([s['shares']*s['price'] for s in portfolio])
44671.15
>>>

>>> # すべての一意の株式名を見つける (セット)
>>> { s['name'] for s in portfolio }
{'MSFT', 'IBM', 'AA', 'GE', 'CAT'}
>>>

>>> # 各株式の総株数をカウントする
>>> totals = { s['name']: 0 for s in portfolio }
>>> for s in portfolio:
        totals[s['name']] += s['shares']

>>> totals
{'AA': 100, 'IBM': 150, 'CAT': 150, 'MSFT': 250, 'GE': 95}
>>>
```
