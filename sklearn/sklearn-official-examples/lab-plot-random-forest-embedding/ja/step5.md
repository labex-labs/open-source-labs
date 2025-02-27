# 変換後のデータに対してナイーブベイズ分類器を学習する

このステップでは、変換後のデータに対してナイーブベイズ分類器を学習します。

```python
nb = BernoulliNB()
nb.fit(X_transformed, y)
```
