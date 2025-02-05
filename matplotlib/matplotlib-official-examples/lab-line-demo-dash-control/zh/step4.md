# 创建绘图

现在，我们可以使用`plt.subplots()`函数来创建绘图。我们还将使用`ax.plot()`函数创建三条线。

```python
fig, ax = plt.subplots()

# 使用set_dashes()和set_capstyle()修改现有线条的虚线样式。
line1, = ax.plot(x, y, label='Using set_dashes() and set_dash_capstyle()')
line1.set_dashes([2, 2, 10, 2])  # 2点长的线，2点的间隔，10点长的线，2点的间隔。
line1.set_dash_capstyle('round')

# 使用plot(..., dashes=...)在创建线条时设置虚线样式。
line2, = ax.plot(x, y - 0.2, dashes=[6, 2], label='Using the dashes parameter')

# 使用plot(..., dashes=..., gapcolor=...)在创建线条时设置虚线样式和交替颜色。
line3, = ax.plot(x, y - 0.4, dashes=[4, 4], gapcolor='tab:pink',
                 label='Using the dashes and gapcolor parameters')

ax.legend(handlelength=4)
plt.show()
```
