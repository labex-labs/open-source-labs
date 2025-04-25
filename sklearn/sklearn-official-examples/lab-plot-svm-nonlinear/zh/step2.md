# 生成数据

在这一步中，我们将生成用于训练和测试支持向量机分类器的数据。我们将生成 300 个具有两个特征的随机数据点。要预测的目标是输入的异或（XOR）。

```python
np.random.seed(0)
X = np.random.randn(300, 2)
Y = np.logical_xor(X[:, 0] > 0, X[:, 1] > 0)
```
