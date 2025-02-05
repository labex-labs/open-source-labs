# 添加带阴影线的椭圆补丁

你也可以在图表中添加带阴影线的补丁。在这种情况下，我们将使用`add_patch`函数向图表中添加一个椭圆补丁。

```python
plt.gca().add_patch(Ellipse((4, 50), 10, 10, fill=True, hatch='*', facecolor='y'))
```
