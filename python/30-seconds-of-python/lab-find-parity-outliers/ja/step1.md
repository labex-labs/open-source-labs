# 偶奇性のアウトライアを見つける

整数のリスト `nums` を引数として受け取り、`nums` に含まれるすべての偶奇性のアウトライアのリストを返す関数 `find_parity_outliers(nums)` を作成します。

この問題を解くには、次の手順をたどることができます。

1. リスト内の偶数と奇数の値をカウントするために、リスト内包表記とともに `collections.Counter` を使用します。
2. 最も一般的な偶奇性を取得するために、`collections.Counter.most_common()` を使用します。
3. 最も一般的な偶奇性と一致しないすべての要素を見つけるために、リスト内包表記を使用します。

```python
from collections import Counter

def find_parity_outliers(nums):
  return [
    x for x in nums
    if x % 2!= Counter([n % 2 for n in nums]).most_common()[0][0]
  ]
```

```python
find_parity_outliers([1, 2, 3, 4, 6]) # [1, 3]
```
