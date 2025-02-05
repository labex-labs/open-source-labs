# 可视化密度估计

最后，我们可以使用直方图和估计的密度函数来可视化密度估计。我们可以绘制原始数据的直方图以及估计的密度函数。

```python
import matplotlib.pyplot as plt

bins = np.linspace(-5, 5, 50)
plt.hist(X, bins=bins, density=True, alpha=0.5, label='Histogram')
plt.plot(X, np.exp(scores), color='red', label='Kernel Density Estimate')
plt.legend()
plt.show()
```
