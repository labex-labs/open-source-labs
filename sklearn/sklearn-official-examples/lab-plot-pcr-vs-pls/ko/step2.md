# 대상 정의

이 예제의 목적상, 작은 분산을 가진 방향과 강하게 상관되는 대상 `y`를 정의합니다. `X`를 두 번째 성분에 투영하고 약간의 노이즈를 추가합니다.

```python
y = X.dot(pca.components_[1]) + rng.normal(size=n_samples) / 2

fig, axes = plt.subplots(1, 2, figsize=(10, 3))

axes[0].scatter(X.dot(pca.components_[0]), y, alpha=0.3)
axes[0].set(xlabel="첫 번째 주성분으로 투영된 데이터", ylabel="y")
axes[1].scatter(X.dot(pca.components_[1]), y, alpha=0.3)
axes[1].set(xlabel="두 번째 주성분으로 투영된 데이터", ylabel="y")
plt.tight_layout()
plt.show()
```
