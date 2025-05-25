# 다중 공선성 특징 처리

특징들이 공선성이 있을 때, 한 특징을 섞어도 상관관계가 있는 다른 특징으로부터 같은 정보를 얻을 수 있기 때문에 모델의 성능에 미치는 영향이 작습니다. 다중 공선성 특징을 처리하는 한 가지 방법은 Spearman 순위 상관관계에 대한 계층적 군집화를 수행하고 임계값을 선택한 후 각 군집에서 하나의 특징만 선택하는 것입니다. 먼저 상관관계가 있는 특징의 히트맵을 그립니다.

```python
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 8))
corr = spearmanr(X).correlation

# 상관 행렬이 대칭이 되도록 합니다.
corr = (corr + corr.T) / 2
np.fill_diagonal(corr, 1)

# 계층적 군집화를 수행하기 전에 상관 행렬을 거리 행렬로 변환합니다.
# Ward 의 연결을 사용하여 계층적 군집화를 수행합니다.
distance_matrix = 1 - np.abs(corr)
dist_linkage = hierarchy.ward(squareform(distance_matrix))
dendro = hierarchy.dendrogram(
    dist_linkage, labels=data.feature_names.tolist(), ax=ax1, leaf_rotation=90
)
dendro_idx = np.arange(0, len(dendro["ivl"]))

ax2.imshow(corr[dendro["leaves"], :][:, dendro["leaves"]])
ax2.set_xticks(dendro_idx)
ax2.set_yticks(dendro_idx)
ax2.set_xticklabels(dendro["ivl"], rotation="vertical")
ax2.set_yticklabels(dendro["ivl"])
fig.tight_layout()
plt.show()
```
