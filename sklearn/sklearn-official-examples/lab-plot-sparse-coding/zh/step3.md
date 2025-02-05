# 生成信号

我们将生成一个信号，并使用 Matplotlib 对其进行可视化。

```python
resolution = 1024
subsampling = 3  # 下采样因子
width = 100
n_components = resolution // subsampling

# 生成一个信号
y = np.linspace(0, resolution - 1, resolution)
first_quarter = y < resolution / 4
y[first_quarter] = 3.0
y[np.logical_not(first_quarter)] = -1.0

# 可视化信号
plt.figure()
plt.plot(y)
plt.title("原始信号")
plt.show()
```
