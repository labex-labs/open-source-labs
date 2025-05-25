# Plotando Dependência Parcial para Duas Características

Neste passo, plotaremos curvas de dependência parcial para as características "idade" e "índice de massa corporal" (IMC) para a árvore de decisão. Com duas características, `PartialDependenceDisplay.from_estimator` espera plotar duas curvas. Aqui, a função de plotagem posiciona uma grade de dois gráficos usando o espaço definido por `ax`.

```python
fig, ax = plt.subplots(figsize=(12, 6))
ax.set_title("Árvore de Decisão")
tree_disp = PartialDependenceDisplay.from_estimator(tree, X, ["age", "bmi"], ax=ax)
```

As curvas de dependência parcial também podem ser plotadas para o perceptron multicamadas. Neste caso, `line_kw` é passado para `PartialDependenceDisplay.from_estimator` para alterar a cor da curva.

```python
fig, ax = plt.subplots(figsize=(12, 6))
ax.set_title("Perceptron Multicamadas")
mlp_disp = PartialDependenceDisplay.from_estimator(
    mlp, X, ["age", "bmi"], ax=ax, line_kw={"color": "red"}
)
```
