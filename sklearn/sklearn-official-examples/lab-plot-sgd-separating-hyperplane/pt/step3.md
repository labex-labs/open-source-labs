# Plotar o hiperplano separador de margem máxima

Finalmente, podemos plotar o hiperplano separador de margem máxima que obtivemos usando o algoritmo SVM com SGD. Criaremos uma grade de pontos usando `np.meshgrid` e, em seguida, computaremos a função de decisão para cada ponto na grade usando o método `decision_function` do modelo SVM. Em seguida, plotaremos a fronteira de decisão usando `plt.contour` e os pontos de dados usando `plt.scatter`.

```python
# plotar a linha, os pontos e os vetores mais próximos ao plano
xx = np.linspace(-1, 5, 10)
yy = np.linspace(-1, 5, 10)

X1, X2 = np.meshgrid(xx, yy)
Z = np.empty(X1.shape)
for (i, j), val in np.ndenumerate(X1):
    x1 = val
    x2 = X2[i, j]
    p = clf.decision_function([[x1, x2]])
    Z[i, j] = p[0]
levels = [-1.0, 0.0, 1.0]
linestyles = ["dashed", "solid", "dashed"]
colors = "k"
plt.contour(X1, X2, Z, levels, colors=colors, linestyles=linestyles)
plt.scatter(X[:, 0], X[:, 1], c=Y, cmap=plt.cm.Paired, edgecolor="black", s=20)

plt.axis("tight")
plt.show()
```
