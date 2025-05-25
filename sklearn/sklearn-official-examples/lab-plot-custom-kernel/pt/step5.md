# Plotar Fronteira de Decisão

Neste passo, plotaremos a superfície de decisão e os vetores de suporte. Usaremos o módulo `DecisionBoundaryDisplay` do módulo de inspeção do scikit-learn para plotar a fronteira de decisão. Também plotaremos os pontos de treinamento usando um gráfico de dispersão.

```python
ax = plt.gca()
DecisionBoundaryDisplay.from_estimator(
    clf,
    X,
    cmap=plt.cm.Paired,
    ax=ax,
    response_method="predict",
    plot_method="pcolormesh",
    shading="auto",
)

plt.scatter(X[:, 0], X[:, 1], c=Y, cmap=plt.cm.Paired, edgecolors="k")
plt.title("Classificação de 3 classes usando Máquina de Vetores de Suporte com kernel personalizado")
plt.axis("tight")
plt.show()
```
