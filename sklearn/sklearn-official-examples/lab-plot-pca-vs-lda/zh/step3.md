# 执行线性判别分析（LDA）

现在，我们将对数据集执行线性判别分析（LDA），以识别能够解释类别之间最大方差的属性。与主成分分析（PCA）不同，LDA是一种使用已知类别标签的监督方法。

```python
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis

lda = LinearDiscriminantAnalysis(n_components=2)
X_r2 = lda.fit(X, y).transform(X)

plt.figure()
for color, i, target_name in zip(colors, [0, 1, 2], target_names):
    plt.scatter(X_r2[y == i, 0], X_r2[y == i, 1], alpha=0.8, color=color, label=target_name)

plt.legend(loc="best", shadow=False, scatterpoints=1)
plt.title("鸢尾花数据集的LDA")
plt.show()
```
