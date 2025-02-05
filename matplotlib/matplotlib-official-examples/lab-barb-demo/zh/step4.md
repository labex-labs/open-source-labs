# 自定义风羽图

我们可以通过更改`barbs`函数的参数来自定义风羽图。例如，我们可以更改向量的长度和枢轴点，为空心风羽填充圆圈，以及更改旗帜和线条的颜色。

```python
plt.barbs(X, Y, U, V, length=8, pivot='middle', fill_empty=True, rounding=False,
          sizes=dict(emptybarb=0.25, spacing=0.2, height=0.3), flagcolor='r',
          barbcolor=['b', 'g'], flip_barb=True, barb_increments=dict(half=10, full=20, flag=100))
plt.show()
```
