# 自定义你的直方图

自定义二维直方图与一维情况类似，你可以控制诸如箱大小或颜色归一化等视觉组件。

```python
fig, axs = plt.subplots(3, 1, figsize=(5, 15), sharex=True, sharey=True,
                        tight_layout=True)

# 我们可以增加每个轴上的箱数
axs[0].hist2d(dist1, dist2, bins=40)

# 以及定义颜色的归一化
axs[1].hist2d(dist1, dist2, bins=40, norm=colors.LogNorm())

# 我们还可以为每个轴定义自定义的箱数
axs[2].hist2d(dist1, dist2, bins=(80, 10), norm=colors.LogNorm())

plt.show()
```
