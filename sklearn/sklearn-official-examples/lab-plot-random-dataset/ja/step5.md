# 2つの情報提供特徴量、クラスごとに2つのクラスタ

2つの情報提供特徴量とクラスごとに2つのクラスタを持つデータセットを作成し、プロットします。

```python
plt.subplot(323)
plt.title("Two informative features, two clusters per class", fontsize="small")
X2, Y2 = make_classification(n_features=2, n_redundant=0, n_informative=2)
plt.scatter(X2[:, 0], X2[:, 1], marker="o", c=Y2, s=25, edgecolor="k")
```
