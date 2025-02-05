# 根据到三角形角点的距离绘制等高线

在这一步中，我们将根据到三角形角点的距离绘制等高线。我们将定义一个关于单个点距离的函数，并根据这个函数绘制等高线。

```python
# 定义一个关于单个点距离的优美函数
def f(x, y, pts):
    z = np.zeros_like(x)
    for p in pts:
        z = z + 1/(np.sqrt((x - p[0])**2 + (y - p[1])**2))
    return 1/z

X, Y = np.meshgrid(np.linspace(-1, 1, 51), np.linspace(-1, 1, 51))
Z = f(X, Y, pts)

CS = plt.contour(X, Y, Z, 20)

tellme('使用鼠标选择等高线标签位置，中间按钮结束')
CL = plt.clabel(CS, manual=True)
```
