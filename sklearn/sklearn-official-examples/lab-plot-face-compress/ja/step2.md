# KBinsDiscretizer を使ったベクトル量子化

ここでは、KBinsDiscretizer を使ってアライグマの顔画像に対してベクトル量子化を行います。画像を表すために 8 つのグレーレベルを使用し、1 ピクセル当たり 3 ビットのみを使用して圧縮することができます。ピクセル値を 8 つのグレーレベルにマッピングするために、一様および k-means クラスタリング戦略を使用します。

#### 一様サンプリング戦略

まず、一様サンプリング戦略を使ってピクセル値を 8 つのグレーレベルにマッピングします。

```python
from sklearn.preprocessing import KBinsDiscretizer

n_bins = 8
encoder = KBinsDiscretizer(
    n_bins=n_bins, encode="ordinal", strategy="uniform", random_state=0
)
compressed_raccoon_uniform = encoder.fit_transform(raccoon_face.reshape(-1, 1)).reshape(
    raccoon_face.shape
)

fig, ax = plt.subplots(ncols=2, figsize=(12, 4))
ax[0].imshow(compressed_raccoon_uniform, cmap=plt.cm.gray)
ax[0].axis("off")
ax[0].set_title("Uniform Sampling")
ax[1].hist(compressed_raccoon_uniform.ravel(), bins=256)
ax[1].set_xlabel("Pixel value")
ax[1].set_ylabel("Count of pixels")
ax[1].set_title("Distribution of the pixel values")
_ = fig.suptitle("Raccoon face compressed using 3 bits and a uniform strategy")
```

#### k-means クラスタリング戦略

次に、k-means クラスタリング戦略を使ってピクセル値を 8 つのグレーレベルにマッピングします。

```python
encoder = KBinsDiscretizer(
    n_bins=n_bins, encode="ordinal", strategy="kmeans", random_state=0
)
compressed_raccoon_kmeans = encoder.fit_transform(raccoon_face.reshape(-1, 1)).reshape(
    raccoon_face.shape
)

fig, ax = plt.subplots(ncols=2, figsize=(12, 4))
ax[0].imshow(compressed_raccoon_kmeans, cmap=plt.cm.gray)
ax[0].axis("off")
ax[0].set_title("K-Means Clustering")
ax[1].hist(compressed_raccoon_kmeans.ravel(), bins=256)
ax[1].set_xlabel("Pixel value")
ax[1].set_ylabel("Count of pixels")
ax[1].set_title("Distribution of the pixel values")
_ = fig.suptitle("Raccoon face compressed using 3 bits and a K-means strategy")
```
