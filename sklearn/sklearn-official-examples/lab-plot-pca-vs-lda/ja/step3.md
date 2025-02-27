# LDA を実行する

次に、クラス間で最も分散をもたらす属性を特定するために、データセットに対して線形判別分析 (Linear Discriminant Analysis: LDA) を実行します。PCA とは異なり、LDA は既知のクラスラベルを使用する教師付き手法です。

```python
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis

lda = LinearDiscriminantAnalysis(n_components=2)
X_r2 = lda.fit(X, y).transform(X)

plt.figure()
for color, i, target_name in zip(colors, [0, 1, 2], target_names):
    plt.scatter(X_r2[y == i, 0], X_r2[y == i, 1], alpha=0.8, color=color, label=target_name)

plt.legend(loc="best", shadow=False, scatterpoints=1)
plt.title("LDA of Iris Dataset")
plt.show()
```
