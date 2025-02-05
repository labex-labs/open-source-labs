# 理论界限（续）

第二张图表明，对于给定数量的样本 `n_samples`，增大可接受的失真 `eps` 能让我们减少最小维度数 `n_components`。

```python
# 可接受失真范围
eps_range = np.linspace(0.01, 0.99, 100)

# 要嵌入的样本数量（观测值）范围
n_samples_range = np.logspace(2, 6, 5)
colors = plt.cm.Blues(np.linspace(0.3, 1.0, len(n_samples_range)))

plt.figure()
for n_samples, color in zip(n_samples_range, colors):
    min_n_components = johnson_lindenstrauss_min_dim(n_samples, eps=eps_range)
    plt.semilogy(eps_range, min_n_components, color=color)

plt.legend([f"n_samples = {n}" for n in n_samples_range], loc="upper right")
plt.xlabel("Distortion eps")
plt.ylabel("Minimum number of dimensions")
plt.title("Johnson-Lindenstrauss bounds:\nn_components vs eps")
plt.show()
```
