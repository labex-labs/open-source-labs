# Collections

`collections` モジュールには、より特殊なデータ操作に役立つさまざまなクラスがあります。たとえば、前の例は `Counter` を使ってこのように解くことができます。

```python
>>> from collections import Counter
>>> totals = Counter()
>>> for s in portfolio:
        totals[s['name']] += s['shares']

>>> totals
Counter({'MSFT': 250, 'IBM': 150, 'CAT': 150, 'AA': 100, 'GE': 95})
>>>
```

`Counter` は、ランキングや数学などの他の種類の操作をサポートしている点で興味深いです。たとえば：

```python
>>> # 最も多く保有されている2つの銘柄を取得する
>>> totals.most_common(2)
[('MSFT', 250), ('IBM', 150)]
>>>

>>> # Counter 同士を加算する
>>> more = Counter()
>>> more['IBM'] = 75
>>> more['AA'] = 200
>>> more['ACME'] = 30
>>> more
Counter({'AA': 200, 'IBM': 75, 'ACME': 30})
>>> totals
Counter({'MSFT': 250, 'IBM': 150, 'CAT': 150, 'AA': 100, 'GE': 95})
>>> totals + more
Counter({'AA': 300, 'MSFT': 250, 'IBM': 225, 'CAT': 150, 'GE': 95, 'ACME': 30})
>>>
```

`defaultdict` オブジェクトは、データをグループ化するために使用できます。たとえば、IBM などの特定の名前に対応するすべての一致するエントリを見つけやすくするために試してみてください。

```python
>>> from collections import defaultdict
>>> byname = defaultdict(list)
>>> for s in portfolio:
        byname[s['name']].append(s)

>>> byname['IBM']
[{'name': 'IBM','shares': 50, 'price': 91.1}, {'name': 'IBM','shares': 100, 'price': 70.44}]
>>> byname['AA']
[{'name': 'AA','shares': 100, 'price': 32.2}]
>>>
```

これが機能する主な機能は、`defaultdict` が自動的に要素を初期化してくれることです。これにより、新しい要素の挿入と `append()` 操作を組み合わせることができます。
