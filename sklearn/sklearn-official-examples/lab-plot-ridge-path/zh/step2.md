# 生成数据

在这一步中，我们将生成一个 10x10 的希尔伯特矩阵，并将目标变量 y 设置为全为 1 的向量。

```python
X = 1.0 / (np.arange(1, 11) + np.arange(0, 10)[:, np.newaxis])
y = np.ones(10)
```
