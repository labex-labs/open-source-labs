# 缩放

在这一步中，我们将对绘图进行缩放。我们将使用`ginput`函数选择缩放框的两个角点，并使用`waitforbuttonpress`函数完成缩放。

```python
tellme('现在进行嵌套缩放，点击开始')
plt.waitforbuttonpress()

while True:
    tellme('选择缩放的两个角点，中间鼠标按钮完成')
    pts = plt.ginput(2, timeout=-1)
    if len(pts) < 2:
        break
    (x0, y0), (x1, y1) = pts
    xmin, xmax = sorted([x0, x1])
    ymin, ymax = sorted([y0, y1])
    plt.xlim(xmin, xmax)
    plt.ylim(ymin, ymax)

tellme('全部完成！')
plt.show()
```
