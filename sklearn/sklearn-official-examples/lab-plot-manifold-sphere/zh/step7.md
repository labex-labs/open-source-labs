# 执行t分布随机邻域嵌入（t-SNE）

最后，我们将执行t分布随机邻域嵌入（t-distributed Stochastic Neighbor Embedding，t-SNE）流形学习。t-SNE是一种技术，它寻求数据的低维表示，这种表示能保留各点之间的局部距离。

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
