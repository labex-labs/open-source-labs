# Darstellung der partiellen Abhängigkeit für ein Merkmal

In diesem Schritt werden wir die partiellen Abhängigkeitskurven für ein einzelnes Merkmal, "age" (Alter), auf den gleichen Achsen darstellen. In diesem Fall wird `tree_disp.axes_` an die zweite Plot-Funktion übergeben.

```python
tree_disp = PartialDependenceDisplay.from_estimator(tree, X, ["age"])
mlp_disp = PartialDependenceDisplay.from_estimator(
    mlp, X, ["age"], ax=tree_disp.axes_, line_kw={"color": "red"}
)
```
