# Isomap 다양체 학습 수행

다음으로 Isomap 다양체 학습을 수행합니다. Isomap 은 모든 쌍의 점 사이의 지오데식 거리를 유지하는 데이터의 저차원 임베딩을 찾는 비선형 차원 축소 기법입니다.

```python
t0 = time()
trans_data = (
    manifold.Isomap(n_neighbors=n_neighbors, n_components=2)
    .fit_transform(sphere_data)
    .T
)
t1 = time()
print("%s: %.2g sec" % ("ISO", t1 - t0))

ax = fig.add_subplot(257)
plt.scatter(trans_data[0], trans_data[1], c=colors, cmap=plt.cm.rainbow)
plt.title("%s (%.2g sec)" % ("Isomap", t1 - t0))
ax.xaxis.set_major_formatter(NullFormatter())
ax.yaxis.set_major_formatter(NullFormatter())
plt.axis("tight")
```
