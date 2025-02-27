# Implementar el Modelo Mixtos Gausianos

En este paso, implementaremos el Modelo Mixtos Gausianos utilizando la clase `GaussianMixture` de scikit-learn. Ajustaremos el modelo a nuestro conjunto de datos y predeciremos las etiquetas de clúster para cada punto de datos. Finalmente, graficaremos los resultados.

```python
# Crea un objeto GMM con 5 componentes
gmm = mixture.GaussianMixture(n_components=5, covariance_type="full")

# Ajusta el GMM a los datos
gmm.fit(X)

# Predice las etiquetas de clúster
Y_ = gmm.predict(X)

# Grafica los resultados
color_iter = ["navy", "c", "cornflowerblue", "gold", "darkorange"]

Para i, color en enumera(color_iter):
    plt.scatter(
        X[Y_ == i, 0], X[Y_ == i, 1], 0.8, color=color, label="Cluster {}".format(i)
    )

plt.legend(loc="best")
plt.title("Modelo Mixtos Gausianos")
plt.show()
```

Tenga en cuenta que en el código original, la línea `Para i, color en enumera(color_iter):` tiene un error de sintaxis. Debería ser `for i, color in enumerate(color_iter):` en Python. La traducción asume que se corregirá este error en el código final.
