# 绘制结果

我们将绘制原始混合信号、原始独立源、通过独立成分分析（ICA）估计的源以及通过主成分分析（PCA）估计的源。

```python
import matplotlib.pyplot as plt

plt.figure()

models = [X, S, S_, H]
names = [
    "观测值（混合信号）",
    "真实源",
    "独立成分分析恢复的信号",
    "主成分分析恢复的信号"
]
colors = ["红色", "钢蓝色", "橙色"]

for ii, (model, name) in enumerate(zip(models, names), 1):
    plt.subplot(4, 1, ii)
    plt.title(name)
    for sig, color in zip(model.T, colors):
        plt.plot(sig, color=color)

plt.tight_layout()
plt.show()
```
