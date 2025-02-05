# 加载图像

我们将使用 `cbook` 中的 `get_sample_data` 方法来加载一张示例图像。此方法返回一个类似文件的对象，我们可以将其传递给 `imshow` 以显示图像。

```python
with cbook.get_sample_data('grace_hopper.jpg') as image_file:
    image = plt.imread(image_file)
```
