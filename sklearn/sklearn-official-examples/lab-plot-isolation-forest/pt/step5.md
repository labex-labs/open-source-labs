# Plotar a Fronteira de Decisão Baseada no Comprimento do Caminho

Definindo `response_method="decision_function"`, o fundo do `DecisionBoundaryDisplay` representa a medida de normalidade de uma observação. Essa pontuação é dada pelo comprimento médio do caminho em uma floresta de árvores aleatórias, que por sua vez é determinada pela profundidade da folha (ou equivalentemente, o número de divisões) necessária para isolar uma amostra específica.

```python
disp = DecisionBoundaryDisplay.from_estimator(
    clf,
    X,
    response_method="decision_function",
    alpha=0.5,
)
disp.ax_.scatter(X[:, 0], X[:, 1], c=y, s=20, edgecolor="k")
disp.ax_.set_title("Fronteira de decisão baseada no comprimento do caminho \ndo IsolationForest")
plt.axis("square")
plt.legend(handles=handles, labels=["outliers", "inliers"], title="classe verdadeira")
plt.colorbar(disp.ax_.collections[1])
plt.show()
```
