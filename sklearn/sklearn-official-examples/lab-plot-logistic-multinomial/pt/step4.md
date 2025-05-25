# Plotar a Fronteira de Decisão do Modelo de Regressão Logística Multinomial

Agora, plotaremos a superfície de decisão do modelo de regressão logística multinomial usando a função `DecisionBoundaryDisplay` do scikit-learn. Definiremos o método de resposta para `"predict"`, o mapa de cores para `"plt.cm.Paired"` e plotaremos também os pontos de treinamento.

```python
_, ax = plt.subplots()
DecisionBoundaryDisplay.from_estimator(
        clf, X, response_method="predict", cmap=plt.cm.Paired, ax=ax
    )
plt.title("Superfície de decisão de LogisticRegression (multinomial)")
plt.axis("tight")

colors = "bry"
for i, color in zip(clf.classes_, colors):
        idx = np.where(y == i)
        plt.scatter(
            X[idx, 0], X[idx, 1], c=color, cmap=plt.cm.Paired, edgecolor="black", s=20
        )
```
