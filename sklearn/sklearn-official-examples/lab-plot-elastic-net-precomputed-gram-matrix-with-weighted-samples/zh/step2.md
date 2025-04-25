# 使用加权样本预计算 Gram 矩阵

为了使用`precompute`选项并结合样本权重来拟合弹性网络（elastic net），我们必须在计算 Gram 矩阵之前，先对设计矩阵进行中心化处理，并通过归一化权重对其进行重新缩放。我们通过从每行中减去每个特征列的加权平均值来对设计矩阵进行中心化。然后，我们将中心化后的设计矩阵的每行乘以相应归一化权重的平方根，从而对其进行重新缩放。最后，我们通过将重新缩放后的设计矩阵与其转置矩阵做点积来计算 Gram 矩阵。

```python
X_offset = np.average(X, axis=0, weights=normalized_weights)
X_centered = X - np.average(X, axis=0, weights=normalized_weights)
X_scaled = X_centered * np.sqrt(normalized_weights)[:, np.newaxis]
gram = np.dot(X_scaled.T, X_scaled)
```
