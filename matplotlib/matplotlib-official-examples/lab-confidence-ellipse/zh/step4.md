# 绘制正相关、负相关和弱相关

现在，我们可以使用这些函数来绘制具有正相关、负相关和弱相关的数据集的置信椭圆。

```python
np.random.seed(0)

PARAMETERS = {
    '正相关': [[0.85, 0.35],
               [0.15, -0.65]],
    '负相关': [[0.9, -0.4],
               [0.1, -0.6]],
    '弱相关': [[1, 0],
               [0, 1]],
}

mu = 2, 4
scale = 3, 5

fig, axs = plt.subplots(1, 3, figsize=(9, 3))
for ax, (title, dependency) in zip(axs, PARAMETERS.items()):
    x, y = get_correlated_dataset(800, dependency, mu, scale)
    ax.scatter(x, y, s=0.5)

    ax.axvline(c='grey', lw=1)
    ax.axhline(c='grey', lw=1)

    confidence_ellipse(x, y, ax, edgecolor='red')

    ax.scatter(mu[0], mu[1], c='red', s=3)
    ax.set_title(title)

plt.show()
```
