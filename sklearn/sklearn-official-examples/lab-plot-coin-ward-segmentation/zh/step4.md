# 绘制结果

最后，我们可以在图像上绘制结果。我们将使用 matplotlib 来绘制缩放后的图像和聚类的轮廓。我们将遍历每个聚类并绘制该聚类中像素的轮廓。

```python
import matplotlib.pyplot as plt

plt.figure(figsize=(5, 5))
plt.imshow(rescaled_coins, cmap=plt.cm.gray)
for l in range(n_clusters):
    plt.contour(
        label == l,
        colors=[
            plt.cm.nipy_spectral(l / float(n_clusters)),
        ],
    )
plt.axis("off")
plt.show()
```
