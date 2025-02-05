# 创建样本权重

我们将创建两组样本权重。第一组样本权重对所有点都是恒定的，第二组样本权重对一些离群点会更大。

```python
sample_weight_last_ten = abs(np.random.randn(len(X)))
sample_weight_constant = np.ones(len(X))
sample_weight_last_ten[15:] *= 5
sample_weight_last_ten[9] *= 15
```
