# 预测估计模型的数据

我们将预测线性模型和 RANSAC 回归器的数据，并比较它们的结果。

```python
# 预测估计模型的数据
line_X = np.arange(X.min(), X.max())[:, np.newaxis]
line_y = lr.predict(line_X)
line_y_ransac = ransac.predict(line_X)
```
