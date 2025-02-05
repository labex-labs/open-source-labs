# 绘制预测概率

现在，我们将绘制网格上每个点的预测概率。我们将创建两个子图：一个用于各向同性RBF核，另一个用于各向异性RBF核。我们将使用`predict_proba`方法来获取网格上每个点的预测概率。然后，我们将预测概率作为彩色图绘制在网格上。我们还将绘制每种鸢尾花的训练点。

```python
titles = ["Isotropic RBF", "Anisotropic RBF"]
plt.figure(figsize=(10, 5))
for i, clf in enumerate((gpc_rbf_isotropic, gpc_rbf_anisotropic)):
    # 绘制预测概率。为此，我们将为网格[x_min, m_max]x[y_min, y_max]中的每个点分配一种颜色。
    plt.subplot(1, 2, i + 1)

    Z = clf.predict_proba(np.c_[xx.ravel(), yy.ravel()])

    # 将结果放入彩色图中
    Z = Z.reshape((xx.shape[0], xx.shape[1], 3))
    plt.imshow(Z, extent=(x_min, x_max, y_min, y_max), origin="lower")

    # 也绘制训练点
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
