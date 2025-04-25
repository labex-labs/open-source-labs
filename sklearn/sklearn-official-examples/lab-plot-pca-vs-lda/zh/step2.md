# 执行主成分分析（PCA）

接下来，我们将对数据集执行主成分分析（PCA），以确定能够解释数据中最大方差的属性组合。我们将在前两个主成分上绘制不同的样本。

```python
from sklearn.decomposition import PCA

pca = PCA(n_components=2)
X_r = pca.fit(X).transform(X)

# 每个成分解释的方差百分比
print("解释的方差比例（前两个成分）：%s" % str(pca.explained_variance_ratio_))

plt.figure()
colors = ["navy", "turquoise", "darkorange"]
lw = 2

for color, i, target_name in zip(colors, [0, 1, 2], target_names):
    plt.scatter(X_r[y == i, 0], X_r[y == i, 1], color=color, alpha=0.8, lw=lw, label=target_name)

plt.legend(loc="best", shadow=False, scatterpoints=1)
plt.title("鸢尾花数据集的 PCA")
plt.show()
```
