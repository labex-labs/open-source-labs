# 生成数据集

接下来，我们将生成一个遵循带噪声正弦曲线的数据集。

```python
# 参数
n_samples = 100

# 生成遵循正弦曲线的随机样本
np.random.seed(0)
X = np.zeros((n_samples, 2))
step = 4.0 * np.pi / n_samples

for i in range(X.shape[0]):
    x = i * step - 6.0
    X[i, 0] = x + np.random.normal(0, 0.1)
    X[i, 1] = 3.0 * (np.sin(x) + np.random.normal(0, 0.2))
```
