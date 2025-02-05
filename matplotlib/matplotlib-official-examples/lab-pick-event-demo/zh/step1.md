# 简单拾取、线条、矩形和文本

我们将通过设置艺术家对象的“picker”属性来启用简单拾取。如果鼠标事件发生在艺术家对象上方，这将使该艺术家对象触发一个拾取事件。我们将创建一个包含一条线、一个矩形和一段文本的简单绘图，并对这些艺术家对象中的每一个启用拾取功能。

```python
fig, (ax1, ax2) = plt.subplots(2, 1)
ax1.set_title('click on points, rectangles or text', picker=True)
ax1.set_ylabel('ylabel', picker=True, bbox=dict(facecolor='red'))
line, = ax1.plot(rand(100), 'o', picker=True, pickradius=5)

# 拾取矩形。
ax2.bar(range(10), rand(10), picker=True)
for label in ax2.get_xticklabels():  # 使x轴刻度标签可拾取。
    label.set_picker(True)
```
