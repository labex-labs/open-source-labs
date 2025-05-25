# 가우시안 혼합 모델

이방성 및 불균일 분산 분포를 처리할 수 있는 가우시안 혼합 모델 (Gaussian Mixture Model) 의 사용법을 살펴볼 것입니다. 다음 코드 블록에서는 `GaussianMixture`를 사용하여 두 번째 및 세 번째 데이터셋을 군집화합니다.

```python
from sklearn.mixture import GaussianMixture

fig, (ax1, ax2) = plt.subplots(nrows=1, ncols=2, figsize=(12, 6))

y_pred = GaussianMixture(n_components=3).fit_predict(X_aniso)
ax1.scatter(X_aniso[:, 0], X_aniso[:, 1], c=y_pred)
ax1.set_title("이방성 분포 볼록")

y_pred = GaussianMixture(n_components=3).fit_predict(X_varied)
ax2.scatter(X_varied[:, 0], X_varied[:, 1], c=y_pred)
ax2.set_title("불균일 분산")

plt.suptitle("가우시안 혼합 클러스터").set_y(0.95)
plt.show()
```
