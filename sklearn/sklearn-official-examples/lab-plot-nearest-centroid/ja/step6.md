# 決定境界を可視化する

Scikit-learn の DecisionBoundaryDisplay 関数を使って、分類器の決定境界を可視化します。

```python
_, ax = plt.subplots()
DecisionBoundaryDisplay.from_estimator(
    clf, X, cmap=cmap_light, ax=ax, response_method="predict"
)
```
