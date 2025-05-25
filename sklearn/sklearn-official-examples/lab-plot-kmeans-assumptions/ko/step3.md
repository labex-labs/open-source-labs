# K-평균 군집화

scikit-learn 의 `KMeans` 클래스를 사용하여 데이터를 군집화할 것입니다. 다음 코드 블록에서는 각 데이터셋에 대한 K-평균으로 얻은 클러스터를 보여주는 2x2 플롯을 만듭니다.

```python
from sklearn.cluster import KMeans

common_params = {
    "n_init": "auto",
    "random_state": random_state,
}

fig, axs = plt.subplots(nrows=2, ncols=2, figsize=(12, 12))

y_pred = KMeans(n_clusters=2, **common_params).fit_predict(X)
axs[0, 0].scatter(X[:, 0], X[:, 1], c=y_pred)
axs[0, 0].set_title("적절하지 않은 클러스터 수")

y_pred = KMeans(n_clusters=3, **common_params).fit_predict(X_aniso)
axs[0, 1].scatter(X_aniso[:, 0], X_aniso[:, 1], c=y_pred)
axs[0, 1].set_title("이방성 분포 볼록")

y_pred = KMeans(n_clusters=3, **common_params).fit_predict(X_varied)
axs[1, 0].scatter(X_varied[:, 0], X_varied[:, 1], c=y_pred)
axs[1, 0].set_title("불균일 분산")

y_pred = KMeans(n_clusters=3, **common_params).fit_predict(X_filtered)
axs[1, 1].scatter(X_filtered[:, 0], X_filtered[:, 1], c=y_pred)
axs[1, 1].set_title("불균일 크기 볼록")

plt.suptitle("예상치 못한 KMeans 클러스터").set_y(0.95)
plt.show()
```
