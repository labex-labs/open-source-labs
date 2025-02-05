# 创建绘图

使用`subplots`函数创建一个2x2的子图网格。然后，使用`plot`函数在每个子图上绘制数据。

```python
fig, axs = plt.subplots(2, 2, layout='constrained')

axs[0, 0].plot(cms, cms)

axs[0, 1].plot(cms, cms, xunits=cm, yunits=inch)

axs[1, 0].plot(cms, cms, xunits=inch, yunits=cm)
axs[1, 0].set_xlim(-1, 4)  # 标量按当前单位解释

axs[1, 1].plot(cms, cms, xunits=inch, yunits=inch)
axs[1, 1].set_xlim(3*cm, 6*cm)  # 厘米被转换为英寸
```
