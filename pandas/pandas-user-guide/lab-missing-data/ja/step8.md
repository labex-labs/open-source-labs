# 欠損値を表す NA スカラーを理解する

最後に、欠損値を表すために使用できる pandas の実験的な `NA` スカラーについて説明します。

```python
s = pd.Series([1, 2, None], dtype="Int64")
s
```
