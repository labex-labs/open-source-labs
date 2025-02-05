# 将图像转换为图

我们将使用 `sklearn.feature_extraction.image` 中的 `img_to_graph` 把图像转换为图。同时，还会计算边上的梯度值。

```python
from sklearn.feature_extraction import image

graph = image.img_to_graph(img, mask=mask)
```
