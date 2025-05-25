# Plotando Dependência Parcial para uma Única Característica

Neste passo, plotaremos as curvas de dependência parcial para uma única característica, "idade", nos mesmos eixos. Neste caso, `tree_disp.axes_` é passado para a segunda função de plotagem.

```python
tree_disp = PartialDependenceDisplay.from_estimator(tree, X, ["age"])
mlp_disp = PartialDependenceDisplay.from_estimator(
    mlp, X, ["age"], ax=tree_disp.axes_, line_kw={"color": "red"}
)
```
