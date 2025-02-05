# 创建加权数据集

我们使用numpy库创建一个加权数据集。我们生成20个具有随机值的点，并为最后10个样本分配更大的权重。

```python
np.random.seed(0)
X = np.r_[np.random.randn(10, 2) + [1, 1], np.random.randn(10, 2)]
y = [1] * 10 + [-1] * 10
sample_weight = 100 * np.abs(np.random.randn(20))
sample_weight[:10] *= 10
```
