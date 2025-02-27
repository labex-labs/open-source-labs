# 画像を再作成する

K-Meansモデルとランダムなコードブックから得たコードブックとラベルを使って、圧縮された画像を再作成します。

```python
def recreate_image(codebook, labels, w, h):
    """コードブックとラベルから（圧縮された）画像を再作成する"""
    return codebook[labels].reshape(w, h, -1)

# 量子化された画像とともに元の画像を表示する
plt.figure()
plt.clf()
plt.axis("off")
plt.title("Original image (96,615 colors)")
plt.imshow(china)

plt.figure()
plt.clf()
plt.axis("off")
plt.title(f"Quantized image ({n_colors} colors, K-Means)")
plt.imshow(recreate_image(kmeans.cluster_centers_, labels, w, h))

plt.figure()
plt.clf()
plt.axis("off")
plt.title(f"Quantized image ({n_colors} colors, Random)")
plt.imshow(recreate_image(codebook_random, labels_random, w, h))

plt.show()
```
