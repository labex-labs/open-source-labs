# 更新直方图颜色

直方图方法返回（除其他外）一个“补丁”对象。这使我们能够访问所绘制对象的属性。利用这一点，我们可以根据自己的喜好编辑直方图。让我们根据每个柱子的 y 值来更改其颜色。

```python
# N 是每个箱中的计数，bins 是箱的下限
N, bins, patches = axs[0].hist(dist1, bins=n_bins)

# 我们将根据高度进行颜色编码，但你可以使用任何标量
fracs = N / N.max()

# 我们需要将数据归一化到 0..1，以适应颜色映射的整个范围
norm = colors.Normalize(fracs.min(), fracs.max())

# 现在，我们将遍历我们的对象并相应地设置每个对象的颜色
for thisfrac, thispatch in zip(fracs, patches):
    color = plt.cm.viridis(norm(thisfrac))
    thispatch.set_facecolor(color)

# 我们也可以通过计数总数对输入进行归一化
axs[1].hist(dist1, bins=n_bins, density=True)

# 现在我们格式化 y 轴以显示百分比
axs[1].yaxis.set_major_formatter(PercentFormatter(xmax=1))

plt.show()
```
