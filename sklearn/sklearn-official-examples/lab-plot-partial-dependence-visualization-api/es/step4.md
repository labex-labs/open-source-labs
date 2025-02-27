# Trazar dependencia parcial para una característica

En este paso, trazaremos las curvas de dependencia parcial para una sola característica, "edad", en los mismos ejes. En este caso, `tree_disp.axes_` se pasa a la segunda función de trazado.

```python
tree_disp = PartialDependenceDisplay.from_estimator(tree, X, ["age"])
mlp_disp = PartialDependenceDisplay.from_estimator(
    mlp, X, ["age"], ax=tree_disp.axes_, line_kw={"color": "red"}
)
```
