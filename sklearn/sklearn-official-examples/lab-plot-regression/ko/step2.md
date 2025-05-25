# 회귀 모델 적합

그런 다음 5 개의 이웃과 균일 및 거리 가중치를 사용하여 샘플 데이터에 회귀 모델을 적합시킵니다. for 루프를 사용하여 각 가중치 유형을 반복하고, 맞춰진 모델의 `predict` 메서드를 사용하여 데이터 포인트의 산점도와 예측 값의 선 그래프를 생성합니다.

```python
n_neighbors = 5

for i, weights in enumerate(["uniform", "distance"]):
    knn = neighbors.KNeighborsRegressor(n_neighbors, weights=weights)
    y_ = knn.fit(X, y).predict(T)

    plt.subplot(2, 1, i + 1)
    plt.scatter(X, y, color="darkorange", label="data")
    plt.plot(T, y_, color="navy", label="prediction")
    plt.axis("tight")
    plt.legend()
    plt.title("KNeighborsRegressor (k = %i, weights = '%s')" % (n_neighbors, weights))

plt.tight_layout()
plt.show()
```
