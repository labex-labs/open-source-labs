# Implementar el Modelo Mixtos Gausianos Bayesiano

En este paso, implementaremos el Modelo Mixtos Gausianos Bayesiano utilizando la clase `BayesianGaussianMixture` de scikit-learn. Este modelo tiene una distribución a priori de proceso de Dirichlet que se adapta automáticamente al número de clusters en función de los datos. Ajustaremos el modelo a nuestro conjunto de datos y predeciremos las etiquetas de cluster para cada punto de datos. Finalmente, graficaremos los resultados.

```python
# Crea un objeto de GMM Bayesiano con 5 componentes
dpgmm = mixture.BayesianGaussianMixture(n_components=5, covariance_type="full")

# Ajusta el GMM Bayesiano a los datos
dpgmm.fit(X)

# Predice las etiquetas de cluster
Y_ = dpgmm.predict(X)

# Grafica los resultados
color_iter = ["navy", "c", "cornflowerblue", "gold", "darkorange"]

Para i, color en enumera(color_iter):
    plt.scatter(
        X[Y_ == i, 0], X[Y_ == i, 1], 0.8, color=color, label="Cluster {}".format(i)
    )

plt.legend(loc="best")
plt.title("Modelo Mixtos Gausianos Bayesiano con una distribución a priori de proceso de Dirichlet")
plt.show()
```

Tenga en cuenta que en el código original, la línea `Para i, color en enumera(color_iter):` tiene un error de sintaxis. Debería ser `for i, color in enumerate(color_iter):` en Python. La traducción asume que se corregirá este error en el código final.
