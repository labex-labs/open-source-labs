# 다차원 스케일링 (MDS) 수행

이제 다차원 스케일링 (MDS) 다양체 학습을 수행합니다. MDS 는 점들 사이의 거리가 원래 고차원 공간의 거리를 반영하는 데이터의 저차원 표현을 찾는 기법입니다.

```python
t0 = time()
mds = manifold.MDS(2, max_iter=100, n_init=1, normalized_stress="auto")
trans_data = mds.fit_transform(sphere_data).T
t1 = time()
print("MDS: %.2g sec" % (t1 - t0))

ax = fig.add_subplot(258)
plt.scatter(trans_data[0], trans_data[1], c=colors, cmap=plt.cm.rainbow)
plt.title("MDS (%.2g sec)" % (t1 - t0))
ax.xaxis.set_major_formatter(NullFormatter())
ax.yaxis.set_major_formatter(NullFormatter())
plt.axis("tight")
```
