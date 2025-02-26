# 演習7.6：lambdaを使ったフィールドによるソート

`lambda` 式を使って、保有株数に基づいてポートフォリオをソートしてみましょう：

```python
>>> portfolio.sort(key=lambda s: s.shares)
>>> for s in portfolio:
        print(s)

... 結果を確認する...
>>>
```

各株式の価格に基づいてポートフォリオをソートしてみましょう

```python
>>> portfolio.sort(key=lambda s: s.price)
>>> for s in portfolio:
        print(s)

... 結果を確認する...
>>>
```

注：`lambda` は便利なショートカットです。なぜなら、`sort()` の呼び出しで直接特殊な処理関数を定義できるからです。これは、まず別の関数を定義する必要があるのとは対照的です。
