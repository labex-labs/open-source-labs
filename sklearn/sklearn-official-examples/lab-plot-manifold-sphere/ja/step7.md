# t-分布確率的近傍埋め込み（t-distributed Stochastic Neighbor Embedding：t-SNE）を実行する

最後に、t-分布確率的近傍埋め込み（t-SNE）によるマニホールド学習を実行します。t-SNE は、点間の局所距離を保つデータの低次元表現を求める手法です。

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
