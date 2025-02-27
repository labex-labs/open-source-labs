# Detección de valores atípicos en datos complejos

Realizaremos la detección de valores atípicos en el conjunto de datos Wine en forma de "plátano". Utilizaremos los mismos tres clasificadores que antes y graficaremos los resultados.

```python
# Aprender una frontera para la detección de valores atípicos con varios clasificadores
xx2, yy2 = np.meshgrid(np.linspace(-1, 5.5, 500), np.linspace(-2.5, 19, 500))
for i, (clf_name, clf) in enumerate(classifiers.items()):
    plt.figure(2)
    clf.fit(X2)
    Z2 = clf.decision_function(np.c_[xx2.ravel(), yy2.ravel()])
    Z2 = Z2.reshape(xx2.shape)
    plt.contour(
        xx2, yy2, Z2, levels=[0], linewidths=2, colors=colors[i]
    )

# Graficar los resultados (= forma de la nube de puntos de datos)
plt.figure(2)  # forma de "plátano"
plt.title("Detección de valores atípicos en un conjunto de datos real (reconocimiento de vinos)")
plt.scatter(X2[:, 0], X2[:, 1], color="black")
plt.xlim((xx2.min(), xx2.max()))
plt.ylim((yy2.min(), yy2.max()))
plt.ylabel("intensidad de color")
plt.xlabel("flavonoides")
plt.show()
```
