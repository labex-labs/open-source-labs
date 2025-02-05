# 生成数据

在这一步中，我们将生成一个10x10的希尔伯特矩阵，并将目标变量y设置为全为1的向量。

```python
X = 1.0 / (np.arange(1, 11) + np.arange(0, 10)[:, np.newaxis])
y = np.ones(10)
```
