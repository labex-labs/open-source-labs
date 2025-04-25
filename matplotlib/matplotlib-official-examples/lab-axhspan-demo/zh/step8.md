# 添加矩形

使用 `axhspan()` 和 `axvspan()` 函数添加一个矩形。

```python
# 一个 50% 灰度的矩形，从 y = 0.25 到 y = 0.75 跨越坐标轴的宽度。
ax.axhspan(0.25, 0.75, facecolor='0.5')
# 一个绿色矩形，从 x = 1.25 到 x = 1.55 跨越坐标轴的高度。
ax.axvspan(1.25, 1.55, facecolor='#2ca02c')
```
