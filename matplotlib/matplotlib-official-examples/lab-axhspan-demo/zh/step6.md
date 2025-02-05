# 添加垂直线

使用 `axvline()` 函数添加垂直线。

```python
# 在 x = 1 处绘制一条跨越 y 范围的垂直线。
ax.axvline(x=1)
# 在 x = 0 处绘制一条跨越 y 范围上半部分的粗蓝线。
ax.axvline(x=0, ymin=0.75, linewidth=8, color='#1f77b4')
```
