# 決定面を可視化する

ここでは、訓練済みモデルの決定面をアイリスデータセット上にプロットします。モデルの決定境界を可視化するために、DecisionBoundaryDisplay クラスを使用します。

```python
from sklearn.inspection import DecisionBoundaryDisplay

ax = plt.gca()
DecisionBoundaryDisplay.from_estimator(
    clf,
    X,
    cmap=plt.cm.Paired,
    ax=ax,
    response_method="predict",
    xlabel=iris.feature_names[0],
    ylabel=iris.feature_names[1],
)
plt.axis("tight")
```
