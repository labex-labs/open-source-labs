# Trazar dependencia parcial para dos características

En este paso, trazaremos curvas de dependencia parcial para las características "edad" y "imc" (índice de masa corporal) para el árbol de decisión. Con dos características, `PartialDependenceDisplay.from_estimator` espera trazar dos curvas. Aquí, la función de trazado coloca una cuadrícula de dos trazados utilizando el espacio definido por `ax`.

```python
fig, ax = plt.subplots(figsize=(12, 6))
ax.set_title("Decision Tree")
tree_disp = PartialDependenceDisplay.from_estimator(tree, X, ["age", "bmi"], ax=ax)
```

Las curvas de dependencia parcial se pueden trazar para la red neuronal multicapa. En este caso, `line_kw` se pasa a `PartialDependenceDisplay.from_estimator` para cambiar el color de la curva.

```python
fig, ax = plt.subplots(figsize=(12, 6))
ax.set_title("Multi-layer Perceptron")
mlp_disp = PartialDependenceDisplay.from_estimator(
    mlp, X, ["age", "bmi"], ax=ax, line_kw={"color": "red"}
)
```
