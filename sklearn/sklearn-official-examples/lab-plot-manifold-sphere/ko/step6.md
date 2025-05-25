# 스펙트럼 임베딩 수행

다음으로 스펙트럼 임베딩 다양체 학습을 수행합니다. 스펙트럼 임베딩은 점들 사이의 쌍대 거리를 보존하는 데이터의 저차원 표현을 찾는 기법입니다.

```python
t0 = time()
se = manifold.SpectralEmbedding(n_components=2, n_neighbors=n_neighbors)
trans_data = se.fit_transform(sphere_data).T
t1 = time()
print("Spectral Embedding: %.2g sec" % (t1 - t0))

ax = fig.add_subplot(259)
plt.scatter(trans_data[0], trans_data[1], c=colors, cmap=plt.cm.rainbow)
plt.title("Spectral Embedding (%.2g sec)" % (t1 - t0))
ax.xaxis.set_major_formatter(NullFormatter())
ax.yaxis.set_major_formatter(NullFormatter())
plt.axis("tight")
```
