# クラスタの可視化

K-Means クラスタリングアルゴリズムを適用した後、形成されたクラスタを可視化しましょう。データポイントとそれぞれのクラスタを可視化するために 3D 散布図を使用します。

```python
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection="3d")
ax.scatter(X[:, 0], X[:, 1], X[:, 2], c=kmeans.labels_)
ax.set_xlabel("Sepal length")
ax.set_ylabel("Sepal width")
ax.set_zlabel("Petal length")
plt.show()
```
