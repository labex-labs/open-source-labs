# 拟合核密度估计器

现在，我们将创建一个 `KernelDensity` 估计器的实例，并将其拟合到我们的数据上。我们可以为估计器选择核的类型和带宽。例如，我们可以使用高斯核，并将带宽设置为 0.2。

```python
kde = KernelDensity(kernel='gaussian', bandwidth=0.2).fit(X)
```
