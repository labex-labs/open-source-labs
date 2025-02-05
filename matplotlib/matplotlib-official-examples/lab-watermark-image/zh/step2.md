# 加载图像

接下来，我们需要加载想要叠加在绘图上的图像。我们可以使用`matplotlib.cbook`模块中的`get_sample_data`方法来加载一张示例图像。在这个例子中，我们将使用`logo2.png`图像。

```python
with cbook.get_sample_data('logo2.png') as file:
    im = image.imread(file)
```
