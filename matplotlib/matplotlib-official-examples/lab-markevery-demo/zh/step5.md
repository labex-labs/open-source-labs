# 创建极坐标图

最后，我们创建一组子图来展示 `markevery` 在极坐标图上的表现。我们注意到其表现与在线性刻度上的表现类似。

```python
# 创建极坐标图
r = np.linspace(0, 3.0, 200)
theta = 2 * np.pi * r

fig, axs = plt.subplots(3, 3, figsize=(10, 6), layout='constrained',
                        subplot_kw={'projection': 'polar'})
for ax, markevery in zip(axs.flat, cases):
    ax.set_title(f'markevery={markevery}')
    ax.plot(theta, r, 'o', ls='-', ms=4, markevery=markevery)
```
