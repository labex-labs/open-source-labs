# データの可視化

散布図を使って Iris データセットを可視化します。がく片の長さとがく片の幅をプロットし、点をそのクラスに基づいて色分けします。

```python
x_min, x_max = X[:, 0].min() - 0.5, X[:, 0].max() + 0.5
y_min, y_max = X[:, 1].min() - 0.5, X[:, 1].max() + 0.5

plt.figure(2, figsize=(8, 6))
plt.clf()

# 学習ポイントをプロットする
plt.scatter(X[:, 0], X[:, 1], c=y, cmap=plt.cm.Set1, edgecolor="k")
plt.xlabel("がく片の長さ")
plt.ylabel("がく片の幅")

plt.xlim(x_min, x_max)
plt.ylim(y_min, y_max)
plt.xticks(())
plt.yticks(())
```
