# 生成新样本

在这一步中，我们将生成新样本，并将它们与原始数据集一起绘制出来。我们将再次使用 `make_blobs` 函数来生成 10 个新样本。

```python
X_new, y_new = make_blobs(
    n_samples=10, centers=[(-7, -1), (-2, 4), (3, 6)], random_state=42
)
```
