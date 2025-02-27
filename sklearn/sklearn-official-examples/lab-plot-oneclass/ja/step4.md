# 結果を可視化する

最後に、1クラスSVMモデルの結果を可視化します。決定境界、学習データ、通常の新奇な観測値、および異常な新奇な観測値をプロットします。

```python
# 結果を可視化する
xx, yy = np.meshgrid(np.linspace(-5, 5, 500), np.linspace(-5, 5, 500))
Z = clf.decision_function(np.c_[xx.ravel(), yy.ravel()])
Z = Z.reshape(xx.shape)

plt.title("Novelty Detection")
plt.contourf(xx, yy, Z, levels=np.linspace(Z.min(), 0, 7), cmap=plt.cm.PuBu)
a = plt.contour(xx, yy, Z, levels=[0], linewidths=2, colors="darkred")
plt.contourf(xx, yy, Z, levels=[0, Z.max()], colors="palevioletred")

s = 40
b1 = plt.scatter(X_train[:, 0], X_train[:, 1], c="white", s=s, edgecolors="k")
b2 = plt.scatter(X_test[:, 0], X_test[:, 1], c="blueviolet", s=s, edgecolors="k")
c = plt.scatter(X_outliers[:, 0], X_outliers[:, 1], c="gold", s=s, edgecolors="k")
plt.axis("tight")
plt.xlim((-5, 5))
plt.ylim((-5, 5))
plt.legend(
    [a.collections[0], b1, b2, c],
    [
        "学習済みの境界",
        "学習観測値",
        "新しい通常の観測値",
        "新しい異常な観測値"
    ],
    loc="upper left",
    prop=matplotlib.font_manager.FontProperties(size=11)
)
plt.xlabel(
    "エラー トレーニング: %d/200 ; エラー 新奇な通常: %d/40 ; エラー 新奇な異常: %d/40"
    % (n_error_train, n_error_test, n_error_outliers)
)
plt.show()
```
