# 创建动画帧

现在我们将为动画创建帧。我们将使用一个 for 循环来生成 60 帧。在循环的每次迭代中，我们将更新 x 和 y 数据，然后使用 `imshow` 方法创建一个新的图像对象。然后，我们将把图像对象追加到 `ims` 列表中。

```python
ims = []
for i in range(60):
    x += np.pi / 15
    y += np.pi / 30
    im = ax.imshow(f(x, y), animated=True)
    if i == 0:
        ax.imshow(f(x, y))  # 先显示初始的一帧
    ims.append([im])
```
