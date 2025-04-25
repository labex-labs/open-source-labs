# 例：1 対多のマッピング

問題：キーを複数の値にマッピングしたい。

```python
portfolio = [
    ('GOOG', 100, 490.1),
    ('IBM', 50, 91.1),
    ('CAT', 150, 83.44),
    ('IBM', 100, 45.23),
    ('GOOG', 75, 572.45),
    ('AA', 50, 23.15)
]
```

前の例と同様に、キー `IBM` は代わりに 2 つの異なるタプルを持つはずである。

解決策：`defaultdict` を使用する。

```python
from collections import defaultdict
holdings = defaultdict(list)
for name, shares, price in portfolio:
    holdings[name].append((shares, price))
holdings['IBM'] # [ (50, 91.1), (100, 45.23) ]
```

`defaultdict` は、キーにアクセスするたびにデフォルト値を取得できるようにします。
