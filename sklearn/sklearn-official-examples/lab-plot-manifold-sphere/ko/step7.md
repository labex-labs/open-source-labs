# t-분포 확률적 이웃 임베딩 (t-SNE) 수행

마지막으로 t-분포 확률적 이웃 임베딩 (t-SNE) 다양체 학습을 수행합니다. t-SNE 는 점들 사이의 국소 거리를 보존하는 데이터의 저차원 표현을 찾는 기법입니다.

```python
t0 = time()
tsne = manifold.TSNE(n_components=2, random_state=0)
trans_data = tsne.fit_transform(sphere_data).T
t1 = time()
print("t-SNE: %.2g sec" % (t1 - t0))

ax = fig.add_subplot(2, 5, 10)
plt.scatter(trans_data[0], trans_data[1], c=colors, cmap=plt.cm.rainbow)
plt.title("t-SNE (%.2g sec)" % (t1 - t0))
ax.xaxis.set_major_formatter(NullFormatter())
ax.yaxis.set_major_formatter(NullFormatter())
plt.axis("tight")

plt.show()
```
