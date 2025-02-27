# 等高線の描画

決定関数の等高線を描画します。まず、`xx` と `yy` 配列を使ってメッシュグリッドを作成します。次に、メッシュグリッドを 2 次元配列に整形し、`SVC` クラスの `decision_function` メソッドを適用して予測値を取得します。そして、`contourf` メソッドを使って等高線を描画します。

```python
YY, XX = np.meshgrid(yy, xx)
xy = np.vstack([XX.ravel(), YY.ravel()]).T
Z = clf.decision_function(xy).reshape(XX.shape)

plt.contourf(XX, YY, Z, cmap=plt.get_cmap("RdBu"), alpha=0.5, linestyles=["-"])

plt.xlim(x_min, x_max)
plt.ylim(y_min, y_max)

plt.xticks(())
plt.yticks(())
```
