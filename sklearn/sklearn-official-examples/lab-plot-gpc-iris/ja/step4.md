# 予測確率のプロット

次に、メッシュ上の各点の予測確率をプロットします。2 つのサブプロットを作成します。1 つは等方性 RBF カーネル用で、もう 1 つは異方性 RBF カーネル用です。メッシュ上の各点の予測確率を取得するために `predict_proba` メソッドを使用します。その後、予測確率をメッシュ上のカラープロットとしてプロットします。また、各種の Iris 花の学習ポイントもプロットします。

```python
titles = ["Isotropic RBF", "Anisotropic RBF"]
plt.figure(figsize=(10, 5))
for i, clf in enumerate((gpc_rbf_isotropic, gpc_rbf_anisotropic)):
    # 予測確率をプロットします。そのために、メッシュ [x_min, m_max]x[y_min, y_max] の各点に色を割り当てます。
    plt.subplot(1, 2, i + 1)

    Z = clf.predict_proba(np.c_[xx.ravel(), yy.ravel()])

    # 結果をカラープロットに入れます
    Z = Z.reshape((xx.shape[0], xx.shape[1], 3))
    plt.imshow(Z, extent=(x_min, x_max, y_min, y_max), origin="lower")

    # 学習ポイントもプロットします
    plt.scatter(X[:, 0], X[:, 1], c=np.array(["r", "g", "b"])[y], edgecolors=(0, 0, 0))
    plt.xlabel("Sepal length")
    plt.ylabel("Sepal width")
    plt.xlim(xx.min(), xx.max())
    plt.ylim(yy.min(), yy.max())
    plt.xticks(())
    plt.yticks(())
    plt.title(
        "%s, LML: %.3f" % (titles[i], clf.log_marginal_likelihood(clf.kernel_.theta))
    )

plt.tight_layout()
plt.show()
```
