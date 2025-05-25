# Detecção de Valores Discrepantes em Dados Bidimensionais

Vamos realizar a detecção de valores discrepantes no conjunto de dados Wine bidimensional. Usaremos três classificadores diferentes para detectar valores discrepantes: Covariância Empírica, Covariância Robusta e One-Class SVM. Em seguida, plotaremos os resultados.

```python
# Treinar uma fronteira para detecção de valores discrepantes com vários classificadores
xx1, yy1 = np.meshgrid(np.linspace(0, 6, 500), np.linspace(1, 4.5, 500))
for i, (clf_name, clf) in enumerate(classifiers.items()):
    plt.figure(1)
    clf.fit(X1)
    Z1 = clf.decision_function(np.c_[xx1.ravel(), yy1.ravel()])
    Z1 = Z1.reshape(xx1.shape)
    plt.contour(
        xx1, yy1, Z1, levels=[0], linewidths=2, colors=colors[i]
    )

# Plotar os resultados (= forma da nuvem de pontos de dados)
plt.figure(1)  # dois clusters
plt.title("Detecção de valores discrepantes em um conjunto de dados real (reconhecimento de vinho)")
plt.scatter(X1[:, 0], X1[:, 1], color="black")
plt.xlim((xx1.min(), xx1.max()))
plt.ylim((yy1.min(), yy1.max()))
plt.ylabel("cinzas")
plt.xlabel("ácido málico")
plt.show()
```
