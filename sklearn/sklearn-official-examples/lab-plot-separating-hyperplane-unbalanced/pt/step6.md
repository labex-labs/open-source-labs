# Plotar as Funções de Decisão para Ambos os Classificadores

Plotaremos as funções de decisão para ambos os classificadores usando a função `DecisionBoundaryDisplay` da biblioteca `sklearn.inspection`. Definiremos `plot_method` para `"contour"`, `colors` para `"k"` para o SVM simples e `"r"` para o SVM ponderado, `levels` para `[0]`, `alpha` para `0.5` e `linestyles` para `["-"]`. Também definiremos `ax` para `plt.gca()`.

```python
ax = plt.gca()
disp = DecisionBoundaryDisplay.from_estimator(
    clf,
    X,
    plot_method="contour",
    colors="k",
    levels=[0],
    alpha=0.5,
    linestyles=["-"],
    ax=ax,
)

wdisp = DecisionBoundaryDisplay.from_estimator(
    wclf,
    X,
    plot_method="contour",
    colors="r",
    levels=[0],
    alpha=0.5,
    linestyles=["-"],
    ax=ax,
)
```
