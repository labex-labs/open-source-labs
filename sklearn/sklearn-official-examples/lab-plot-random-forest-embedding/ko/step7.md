# 원본 데이터와 축소된 데이터의 산점도

이 단계에서는 원본 데이터와 축소된 데이터의 산점도를 생성합니다.

```python
fig = plt.figure(figsize=(9, 8))

ax = plt.subplot(221)
ax.scatter(X[:, 0], X[:, 1], c=y, s=50, edgecolor="k")
ax.set_title("원본 데이터 (2 차원)")
ax.set_xticks(())
ax.set_yticks(())

ax = plt.subplot(222)
ax.scatter(X_reduced[:, 0], X_reduced[:, 1], c=y, s=50, edgecolor="k")
ax.set_title(
    "변환된 데이터의 축소된 SVD (2 차원) (%dd)" % X_transformed.shape[1]
)
ax.set_xticks(())
ax.set_yticks(())
```
