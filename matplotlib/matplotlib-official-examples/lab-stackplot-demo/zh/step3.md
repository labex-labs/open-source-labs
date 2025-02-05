# 创建流图

第三步是使用 `stackplot()` 函数创建一个流图，并将 `baseline` 参数设置为 'wiggle'。我们将创建一个高斯混合随机数据集，并将其绘制成流图。

```python
# 固定随机状态以确保可重复性
np.random.seed(19680801)


def gaussian_mixture(x, n=5):
    """返回在位置 *x* 处计算的 *n* 个高斯分布的随机混合。"""
    def add_random_gaussian(a):
        amplitude = 1 / (.1 + np.random.random())
        dx = x[-1] - x[0]
        x0 = (2 * np.random.random() -.5) * dx
        z = 10 / (.1 + np.random.random()) / dx
        a += amplitude * np.exp(-(z * (x - x0))**2)
    a = np.zeros_like(x)
    for j in range(n):
        add_random_gaussian(a)
    return a


x = np.linspace(0, 100, 101)
ys = [gaussian_mixture(x) for _ in range(3)]

fig, ax = plt.subplots()
ax.stackplot(x, ys, baseline='wiggle')
plt.show()
```
