# Detección de valores atípicos en datos bidimensionales

Realizaremos la detección de valores atípicos en el conjunto de datos bidimensional Wine. Utilizaremos tres clasificadores diferentes para detectar valores atípicos: Covarianza Empírica, Covarianza Robusta y SVM de una clase. Luego graficaremos los resultados.

```python
# Aprender una frontera para la detección de valores atípicos con varios clasificadores
xx1, yy1 = np.meshgrid(np.linspace(0, 6, 500), np.linspace(1, 4.5, 500))
for i, (clf_name, clf) in enumerate(classifiers.items()):
    plt.figure(1)
    clf.fit(X1)
    Z1 = clf.decision_function(np.c_[xx1.ravel(), yy1.ravel()])
    Z1 = Z1.reshape(xx1.shape)
    plt.contour(
        xx1, yy1, Z1, levels=[0], linewidths=2, colors=colors[i]
    )

# Graficar los resultados (= forma de la nube de puntos de datos)
plt.figure(1)  # dos clusters
plt.title("Detección de valores atípicos en un conjunto de datos real (reconocimiento de vinos)")
plt.scatter(X1[:, 0], X1[:, 1], color="black")
plt.xlim((xx1.min(), xx1.max()))
plt.ylim((yy1.min(), yy1.max()))
plt.ylabel("ceniza")
plt.xlabel("ácido málico")
plt.show()
```
