# 結果をプロットする

2 つの回帰器の性能を比較するために、結果をプロットします。`matplotlib`を使用して、実際のテストデータ、ランダムフォレスト回帰器による予測、および多次元出力回帰器による予測の散布図を作成します。

```python
plt.figure()
s = 50
a = 0.4
plt.scatter(y_test[:, 0], y_test[:, 1], edgecolor="k", c="navy", s=s, marker="s", alpha=a, label="Data")
plt.scatter(y_rf[:, 0], y_rf[:, 1], edgecolor="k", c="c", s=s, marker="^", alpha=a, label="RF score=%.2f" % regr_rf.score(X_test, y_test))
plt.scatter(y_multirf[:, 0], y_multirf[:, 1], edgecolor="k", c="cornflowerblue", s=s, alpha=a, label="Multi RF score=%.2f" % regr_multirf.score(X_test, y_test))
plt.xlim([-6, 6])
plt.ylim([-6, 6])
plt.xlabel("target 1")
plt.ylabel("target 2")
plt.title("Comparing Random Forests and the Multi-Output Meta Estimator")
plt.legend()
plt.show()
```
