# 使用 rcParams 设置标题的 Y 轴位置

设置`rcParams`的`titley`和`titlepad`参数来调整标题的垂直位置。

```python
fig, ax = plt.subplots()
ax.plot(range(10))
ax.xaxis.set_label_position('top')
ax.set_xlabel('X-label')
plt.rcParams['axes.titley'] = 1.0
plt.rcParams['axes.titlepad'] = -14
ax.set_title('RCParam Y Positioning')
```
