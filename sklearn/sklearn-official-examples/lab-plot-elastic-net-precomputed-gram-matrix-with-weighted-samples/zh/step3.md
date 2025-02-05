# 拟合弹性网络

现在我们可以进行拟合了。我们必须将中心化后的设计矩阵传递给`fit`，以防止弹性网络估计器检测到它未中心化并丢弃我们传递的Gram矩阵。但是，如果我们传递缩放后的设计矩阵，预处理代码会错误地再次对其进行缩放。我们还将归一化权重传递给`fit`函数的`sample_weight`参数。

```python
from sklearn.linear_model import ElasticNet

lm = ElasticNet(alpha=0.01, precompute=gram)
lm.fit(X_centered, y, sample_weight=normalized_weights)
```
