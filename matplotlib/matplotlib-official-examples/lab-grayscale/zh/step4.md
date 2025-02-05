# 定义图像和补丁示例函数

我们定义了 `image_and_patch_example` 函数，该函数以一个轴对象为输入，绘制一幅随机图像，并在图中添加一个补丁。

```python
def image_and_patch_example(ax):
    ax.imshow(np.random.random(size=(20, 20)), interpolation='none')
    c = plt.Circle((5, 5), radius=5, label='patch')
    ax.add_patch(c)
```
