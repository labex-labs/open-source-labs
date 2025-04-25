# 创建数据

我们将创建一个包含 20 个点的数据集，其中前 10 个点属于类别 1，后 10 个点属于类别 -1。

```python
np.random.seed(0)
X = np.r_[np.random.randn(10, 2) + [1, 1], np.random.randn(10, 2)]
y = [1] * 10 + [-1] * 10
```
