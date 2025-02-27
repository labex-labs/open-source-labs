# モデルの評価

訓練済みのモデルをテストデータと外れ値データで評価します。`predict` メソッドを使用して、テストデータと外れ値データのラベルを予測します。その後、テストデータと外れ値データにおける誤りの数をカウントします。

```python
y_pred_test = clf.predict(X_test)
y_pred_outliers = clf.predict(X_outliers)
n_error_test = y_pred_test[y_pred_test == -1].size
n_error_outliers = y_pred_outliers[y_pred_outliers == 1].size
```
