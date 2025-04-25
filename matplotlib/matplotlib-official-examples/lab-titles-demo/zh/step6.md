# 手动设置标题的 Y 轴位置

通过使用`title()`函数的`y`参数来手动指定标题的垂直位置。

```python
fig, ax = plt.subplots()
ax.plot(range(10))
ax.xaxis.set_label_position('top')
ax.set_xlabel('X-label')
ax.set_title('Manual Y Positioning', y=1.0)
```
