# KBinsDiscretizer 를 이용한 벡터 양자화

이제 KBinsDiscretizer 를 사용하여 족제비 얼굴 이미지에 대한 벡터 양자화를 수행합니다. 이미지를 나타내는 데 8 개의 회색 레벨을 사용하며, 이는 각 픽셀당 3 비트만 사용하여 압축할 수 있습니다. 픽셀 값을 8 개의 회색 레벨로 매핑하기 위해 균일 및 k-평균 클러스터링 전략을 사용할 것입니다.

#### 균일 샘플링 전략

먼저 균일 샘플링 전략을 사용하여 픽셀 값을 8 개의 회색 레벨로 매핑합니다.

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
ax[0].set_title("균일 샘플링")
ax[1].hist(compressed_raccoon_uniform.ravel(), bins=256)
ax[1].set_xlabel("픽셀 값")
ax[1].set_ylabel("픽셀 개수")
ax[1].set_title("픽셀 값 분포")
_ = fig.suptitle("균일 전략을 사용하여 3 비트로 압축된 족제비 얼굴 이미지")
```

#### K-평균 클러스터링 전략

이제 k-평균 클러스터링 전략을 사용하여 픽셀 값을 8 개의 회색 레벨로 매핑합니다.

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
ax[0].set_title("K-평균 클러스터링")
ax[1].hist(compressed_raccoon_kmeans.ravel(), bins=256)
ax[1].set_xlabel("픽셀 값")
ax[1].set_ylabel("픽셀 개수")
ax[1].set_title("픽셀 값 분포")
_ = fig.suptitle("K-평균 전략을 사용하여 3 비트로 압축된 족제비 얼굴 이미지")
```
