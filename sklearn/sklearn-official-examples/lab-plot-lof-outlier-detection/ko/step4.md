# 결과 시각화

이상치 점수에 비례하는 반경을 가진 원으로 데이터 포인트를 플롯합니다.

```python
plt.scatter(X[:, 0], X[:, 1], color="k", s=3.0, label="Data points")
# 이상치 점수에 비례하는 반경으로 원을 플롯합니다.
radius = (X_scores.max() - X_scores) / (X_scores.max() - X_scores.min())
scatter = plt.scatter(
    X[:, 0],
    X[:, 1],
    s=1000 * radius,
    edgecolors="r",
    facecolors="none",
    label="Outlier scores",
)
plt.axis("tight")
plt.xlim((-5, 5))
plt.ylim((-5, 5))
plt.xlabel("이상치 탐지")
plt.legend(
    handler_map={scatter: HandlerPathCollection(update_func=update_legend_marker_size)}
)
plt.title("Local Outlier Factor (LOF)")
plt.show()
```
