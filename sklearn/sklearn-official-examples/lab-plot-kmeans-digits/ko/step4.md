# PCA 축소 데이터에서 결과 시각화

PCA 를 사용하여 데이터셋을 2 차원으로 축소하고 이 새로운 공간에서 데이터와 클러스터를 플롯합니다.

```python
import matplotlib.pyplot as plt

reduced_data = PCA(n_components=2).fit_transform(data)
kmeans = KMeans(init="k-means++", n_clusters=n_digits, n_init=4)
kmeans.fit(reduced_data)

# 메쉬의 간격. VQ 의 품질을 높이려면 감소.
h = 0.02  # 메쉬 [x_min, x_max]x[y_min, y_max] 의 점.

# 결정 경계를 플롯합니다. 각 점에 색상을 할당합니다.
x_min, x_max = reduced_data[:, 0].min() - 1, reduced_data[:, 0].max() + 1
y_min, y_max = reduced_data[:, 1].min() - 1, reduced_data[:, 1].max() + 1
xx, yy = np.meshgrid(np.arange(x_min, x_max, h), np.arange(y_min, y_max, h))

# 메쉬의 각 점에 대한 레이블을 가져옵니다. 마지막으로 학습된 모델을 사용합니다.
Z = kmeans.predict(np.c_[xx.ravel(), yy.ravel()])

# 결과를 색상 플롯에 넣습니다.
Z = Z.reshape(xx.shape)
plt.figure(1)
plt.clf()
plt.imshow(
    Z,
    interpolation="nearest",
    extent=(xx.min(), xx.max(), yy.min(), yy.max()),
    cmap=plt.cm.Paired,
    aspect="auto",
    origin="lower",
)

plt.plot(reduced_data[:, 0], reduced_data[:, 1], "k.", markersize=2)
# 중심점을 흰색 X 로 플롯합니다.
centroids = kmeans.cluster_centers_
plt.scatter(
    centroids[:, 0],
    centroids[:, 1],
    marker="x",
    s=169,
    linewidths=3,
    color="w",
    zorder=10,
)
plt.title(
    "숫자 데이터셋에 대한 K-평균 군집화 (PCA 축소 데이터)\n"
    "중심점은 흰색 십자표시로 표시됨"
)
plt.xlim(x_min, x_max)
plt.ylim(y_min, y_max)
plt.xticks(())
plt.yticks(())
plt.show()
```
