# 多次元尺度法（Multi-dimensional Scaling：MDS）を実行する

次に、多次元尺度法（MDS）によるマニホールド学習を実行します。MDSは、点間の距離が元の高次元空間の距離を反映するような、データの低次元表現を求める手法です。

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
