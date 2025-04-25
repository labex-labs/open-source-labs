# 演習 7.5：フィールドによるソート

株式名で辞書式にポートフォリオデータをソートする次の文を試してみましょう。

```python
>>> def stock_name(s):
       return s.name

>>> portfolio.sort(key=stock_name)
>>> for s in portfolio:
           print(s)

... 結果を確認する...
>>>
```

この部分では、`stock_name()` 関数は `portfolio` リストの単一のエントリから株式の名前を抽出します。`sort()` はこの関数の結果を比較に使用します。
