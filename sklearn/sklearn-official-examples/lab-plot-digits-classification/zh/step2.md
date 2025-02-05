# 加载并可视化数字数据集

我们将加载数字数据集，该数据集由8x8像素的数字图像组成。我们将使用`matplotlib`的`imshow()`方法来可视化前4张图像及其对应的标签。

```python
digits = datasets.load_digits()

_, axes = plt.subplots(nrows=1, ncols=4, figsize=(10, 3))
for ax, image, label in zip(axes, digits.images, digits.target):
    ax.set_axis_off()
    ax.imshow(image, cmap=plt.cm.gray_r, interpolation="nearest")
    ax.set_title("Training: %i" % label)
```
