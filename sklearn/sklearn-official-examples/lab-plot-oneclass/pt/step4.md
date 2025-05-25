# Visualizar os resultados

Finalmente, visualizaremos os resultados do modelo SVM de uma classe. Iremos plotar a fronteira de decisão, os dados de treino, as observações regulares e novas, e as observações novas anormais.

```python
# Visualizar os resultados
xx, yy = np.meshgrid(np.linspace(-5, 5, 500), np.linspace(-5, 5, 500))
Z = clf.decision_function(np.c_[xx.ravel(), yy.ravel()])
Z = Z.reshape(xx.shape)

plt.title("Detecção de Novidades")
plt.contourf(xx, yy, Z, levels=np.linspace(Z.min(), 0, 7), cmap=plt.cm.PuBu)
a = plt.contour(xx, yy, Z, levels=[0], linewidths=2, colors="darkred")
plt.contourf(xx, yy, Z, levels=[0, Z.max()], colors="palevioletred")

s = 40
b1 = plt.scatter(X_train[:, 0], X_train[:, 1], c="white", s=s, edgecolors="k")
b2 = plt.scatter(X_test[:, 0], X_test[:, 1], c="blueviolet", s=s, edgecolors="k")
c = plt.scatter(X_outliers[:, 0], X_outliers[:, 1], c="gold", s=s, edgecolors="k")
plt.axis("tight")
plt.xlim((-5, 5))
plt.ylim((-5, 5))
plt.legend(
    [a.collections[0], b1, b2, c],
    [
        "fronteira aprendida",
        "observações de treino",
        "observações regulares novas",
        "observações anormais novas",
    ],
    loc="upper left",
    prop=matplotlib.font_manager.FontProperties(size=11),
)
plt.xlabel(
    "erro treino: %d/200 ; erros novos regulares: %d/40 ; erros novos anormais: %d/40"
    % (n_error_train, n_error_test, n_error_outliers)
)
plt.show()
```
