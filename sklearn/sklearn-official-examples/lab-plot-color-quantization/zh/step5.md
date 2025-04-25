# 重建图像

我们将使用从 K 均值模型和随机码本获得的码本和标签来重建压缩图像。

```python
def recreate_image(codebook, labels, w, h):
    """从码本和标签重建（压缩）图像"""
    return codebook[labels].reshape(w, h, -1)

# 将原始图像与量化后的图像并排显示
plt.figure()
plt.clf()
plt.axis("off")
plt.title("原始图像 (96,615 种颜色)")
plt.imshow(china)

plt.figure()
plt.clf()
plt.axis("off")
plt.title(f"量化图像 ({n_colors} 种颜色，K 均值)")
plt.imshow(recreate_image(kmeans.cluster_centers_, labels, w, h))

plt.figure()
plt.clf()
plt.axis("off")
plt.title(f"量化图像 ({n_colors} 种颜色，随机)")
plt.imshow(recreate_image(codebook_random, labels_random, w, h))

plt.show()
```
