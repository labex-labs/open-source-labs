# 给数据添加噪声

然后，我们将使用numpy给数据点之间的成对距离添加噪声。

```python
similarities = euclidean_distances(X_true)

# 给相似度添加噪声
noise = np.random.rand(n_samples, n_samples)
noise = noise + noise.T
noise[np.arange(noise.shape[0]), np.arange(noise.shape[0])] = 0
similarities += noise
```
