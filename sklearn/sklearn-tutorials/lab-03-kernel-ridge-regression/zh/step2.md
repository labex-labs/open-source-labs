# 生成合成数据

接下来，让我们生成一些用于实验的合成数据。我们将创建一个正弦目标函数，并给它添加一些随机噪声。

```python
# 生成输入数据
np.random.seed(0)
X = np.sort(5 * np.random.rand(100, 1), axis=0)
y = np.sin(X).ravel()
y += 0.5 * (0.5 - np.random.rand(y.size))
```
