# 创建动画

我们将使用一个 for 循环来遍历动画的每一帧。在每次迭代中，我们将清除坐标轴，绘制当前帧，设置标题，并暂停一小段时间以显示动画。

```python
fig, ax = plt.subplots()

for i, img in enumerate(data):
    ax.clear()
    ax.imshow(img)
    ax.set_title(f"frame {i}")
    plt.pause(0.1)
```
