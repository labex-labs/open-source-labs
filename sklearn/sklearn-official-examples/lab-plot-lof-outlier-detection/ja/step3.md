# アウトライア検出のためのモデルの適合

アウトライア検出のためのモデルを適合させ、訓練サンプルの予測ラベルを計算するために `LocalOutlierFactor` を使用します。

```python
clf = LocalOutlierFactor(n_neighbors=20, contamination=0.1)
y_pred = clf.fit_predict(X)
X_scores = clf.negative_outlier_factor_
```
