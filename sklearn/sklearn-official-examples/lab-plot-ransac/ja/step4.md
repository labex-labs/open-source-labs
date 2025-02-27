# 推定モデルのデータ予測

線形モデルと RANSAC 回帰器のデータを予測し、それらの結果を比較します。

```python
# Predict data of estimated models
line_X = np.arange(X.min(), X.max())[:, np.newaxis]
line_y = lr.predict(line_X)
line_y_ransac = ransac.predict(line_X)
```
