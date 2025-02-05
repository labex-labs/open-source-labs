# 自定义图表

为了使图表包含更多信息，我们可以通过添加标签、标题以及反转 y 轴来对其进行自定义。

```python
ax.set_yticks(y_pos, labels=people)
ax.invert_yaxis()  # labels read top-to-bottom
ax.set_xlabel('Performance')
ax.set_title('How fast do you want to go today?')
```
