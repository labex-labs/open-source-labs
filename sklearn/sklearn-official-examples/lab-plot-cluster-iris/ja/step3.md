# データの可視化

K-Means クラスタリングアルゴリズムを適用する前に、まずデータを可視化して、それをよりよく理解しましょう。データを可視化するために 3D 散布図を使用します。

```python
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection="3d")
ax.scatter(X[:, 0], X[:, 1], X[:, 2])
ax.set_xlabel("Sepal length")
ax.set_ylabel("Sepal width")
ax.set_zlabel("Petal length")
plt.show()
```
