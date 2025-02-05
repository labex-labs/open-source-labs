# 创建带有超链接的图像

在这一步中，我们将创建一幅图像并为其添加一个超链接。以下是创建图像的代码：

```python
fig = plt.figure()
delta = 0.025
x = y = np.arange(-3.0, 3.0, delta)
X, Y = np.meshgrid(x, y)
Z1 = np.exp(-X**2 - Y**2)
Z2 = np.exp(-(X - 1)**2 - (Y - 1)**2)
Z = (Z1 - Z2) * 2

im = plt.imshow(Z, interpolation='bilinear', cmap=cm.gray,
                origin='lower', extent=[-3, 3, -3, 3])
```

要为图像添加超链接，我们需要使用图像对象的 `set_url()` 方法。此方法将一个URL作为其参数。以下是更新后的代码：

```python
im.set_url('https://www.google.com/')
```

该图像将具有指向 `https://www.google.com/` 的超链接。最后，我们可以使用 `fig.savefig()` 将图表保存为SVG文件：

```python
fig.savefig('image.svg')
```
