# Plotar Resultados

Vamos representar graficamente os pontos de dados com círculos cujo raio é proporcional às pontuações de outlier.

```python
plt.scatter(X[:, 0], X[:, 1], color="k", s=3.0, label="Pontos de dados")
# plotar círculos com raio proporcional às pontuações de outlier
radius = (X_scores.max() - X_scores) / (X_scores.max() - X_scores.min())
scatter = plt.scatter(
    X[:, 0],
    X[:, 1],
    s=1000 * radius,
    edgecolors="r",
    facecolors="none",
    label="Pontuações de Outlier",
)
plt.axis("tight")
plt.xlim((-5, 5))
plt.ylim((-5, 5))
plt.xlabel("Detecção de Outliers")
plt.legend(
    handler_map={scatter: HandlerPathCollection(update_func=update_legend_marker_size)}
)
plt.title("Fator Local de Outlier (LOF)")
plt.show()
```
