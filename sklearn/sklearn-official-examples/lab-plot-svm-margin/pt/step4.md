# Calcular Margens

Calculamos as margens para o hiperplano separador. Primeiro, calculamos a distância da margem usando os coeficientes do modelo. Em seguida, calculamos a distância vertical dos vetores de suporte ao hiperplano usando a inclinação do hiperplano. Finalmente, plotamos a linha, os pontos e os vetores mais próximos do plano.

```python
margin = 1 / np.sqrt(np.sum(clf.coef_**2))
yy_down = yy - np.sqrt(1 + a**2) * margin
yy_up = yy + np.sqrt(1 + a**2) * margin

plt.plot(xx, yy, "k-")
plt.plot(xx, yy_down, "k--")
plt.plot(xx, yy_up, "k--")

plt.scatter(
    clf.support_vectors_[:, 0],
    clf.support_vectors_[:, 1],
    s=80,
    facecolors="none",
    zorder=10,
    edgecolors="k",
    cmap=plt.get_cmap("RdBu"),
)
plt.scatter(
    X[:, 0], X[:, 1], c=Y, zorder=10, cmap=plt.get_cmap("RdBu"), edgecolors="k"
)

plt.axis("tight")
x_min = -4.8
x_max = 4.2
y_min = -6
y_max = 6
```
