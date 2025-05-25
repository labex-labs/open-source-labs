# 종 분포 예측

이 단계에서는 OneClassSVM 모델을 사용하여 종 분포를 예측합니다. 학습 데이터를 사용하여 종 분포를 예측하고 결과를 플롯합니다.

```python
# 학습 데이터를 사용하여 종 분포 예측
Z = np.ones((data.Ny, data.Nx), dtype=np.float64)

# 육지 지점에 대해서만 예측합니다.
idx = np.where(data.coverages[6] > -9999)
coverages_land = data.coverages[:, idx[0], idx[1]].T

pred = clf.decision_function((coverages_land - mean) / std)
Z *= pred.min()
Z[idx[0], idx[1]] = pred

levels = np.linspace(Z.min(), Z.max(), 25)
Z[data.coverages[6] == -9999] = -9999

# 예측 결과의 등고선 플롯
plt.contourf(X, Y, Z, levels=levels, cmap=plt.cm.Reds)
plt.colorbar(format="%.2f")

# 학습/테스트 지점 산점도
plt.scatter(
    BV_bunch.pts_train["dd long"],
    BV_bunch.pts_train["dd lat"],
    s=2**2,
    c="black",
    marker="^",
    label="train",
)
plt.scatter(
    BV_bunch.pts_test["dd long"],
    BV_bunch.pts_test["dd lat"],
    s=2**2,
    c="black",
    marker="x",
    label="test",
)
plt.legend()
plt.title(BV_bunch.name)
plt.axis("equal")
```
