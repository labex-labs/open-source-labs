# 生成矩形的角点

为了使用矩形绘制我们的直方图，我们需要计算每个矩形的角点。添加以下代码：

```python
left = bins[:-1]
right = bins[1:]
bottom = np.zeros(len(left))
top = bottom + n
```
