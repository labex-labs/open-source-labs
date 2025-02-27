# エラーの数を計算する

学習データ、通常の新奇な観測値、および異常な新奇な観測値に対して、モデルが犯すエラーの数を計算します。

```python
# エラーの数をカウントする
n_error_train = y_pred_train[y_pred_train == -1].size
n_error_test = y_pred_test[y_pred_test == -1].size
n_error_outliers = y_pred_outliers[y_pred_outliers == 1].size
```
