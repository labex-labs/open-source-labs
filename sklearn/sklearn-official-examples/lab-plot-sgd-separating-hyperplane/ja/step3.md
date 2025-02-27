# 最大マージンを分離するハイパープレーンを描画する

最後に、SGDを使ったSVMアルゴリズムで得た最大マージンを分離するハイパープレーンを描画することができます。`np.meshgrid`を使って点のグリッドを作成し、その後、SVMモデルの`decision_function`メソッドを使ってグリッド上の各点に対する決定関数を計算します。その後、`plt.contour`を使って決定境界を描画し、`plt.scatter`を使ってデータポイントを描画します。

```python
# plot the line, the points, and the nearest vectors to the plane
xx = np.linspace(-1, 5, 10)
yy = np.linspace(-1, 5, 10)

X1, X2 = np.meshgrid(xx, yy)
Z = np.empty(X1.shape)
for (i, j), val in np.ndenumerate(X1):
    x1 = val
    x2 = X2[i, j]
    p = clf.decision_function([[x1, x2]])
    Z[i, j] = p[0]
levels = [-1.0, 0.0, 1.0]
linestyles = ["dashed", "solid", "dashed"]
colors = "k"
plt.contour(X1, X2, Z, levels, colors=colors, linestyles=linestyles)
plt.scatter(X[:, 0], X[:, 1], c=Y, cmap=plt.cm.Paired, edgecolor="black", s=20)

plt.axis("tight")
plt.show()
```
