# 设置图例样式

最后，我们可以设置图例的样式，使其在视觉上更具吸引力。我们使用 `get_frame` 函数获取图例的框架，然后使用 `set_facecolor` 函数设置框架的背景颜色。

```python
# 为图例设置一个更好看的背景颜色。
legend.get_frame().set_facecolor('C0')
```
