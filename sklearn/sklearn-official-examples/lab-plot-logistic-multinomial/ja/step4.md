# 多項ロジスティック回帰モデルの決定境界の描画

ここでは、scikit-learnの`DecisionBoundaryDisplay`関数を使って、多項ロジスティック回帰モデルの決定面を描画します。応答方法を`"predict"`に、カラーマップを`"plt.cm.Paired"`に設定し、学習ポイントも描画します。

```python
_, ax = plt.subplots()
DecisionBoundaryDisplay.from_estimator(
        clf, X, response_method="predict", cmap=plt.cm.Paired, ax=ax
    )
plt.title("Decision surface of LogisticRegression (multinomial)")
plt.axis("tight")

colors = "bry"
for i, color in zip(clf.classes_, colors):
        idx = np.where(y == i)
        plt.scatter(
            X[idx, 0], X[idx, 1], c=color, cmap=plt.cm.Paired, edgecolor="black", s=20
        )
```
