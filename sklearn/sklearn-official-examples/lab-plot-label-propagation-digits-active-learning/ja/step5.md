# 最も不確定なポイントにラベルを付ける

人間によるラベルを、ラベル付きのデータポイントに追加し、それらを使ってモデルを学習します。

```python
y_train[uncertainty_index] = y[uncertainty_index]
lp_model.fit(X, y_train)
```
