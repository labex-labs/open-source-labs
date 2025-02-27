# Graficar la estimación de densidad

Ahora graficaremos la estimación de densidad de la mezcla de gaussianas. Crearemos una malla de puntos en el rango del conjunto de datos y calcularemos la negativa del log-verosimilitud predicha por el GMM para cada punto. Luego mostraremos las puntuaciones predichas como un gráfico de contornos y un diagrama de dispersión de los datos de entrenamiento.

```python
# mostrar las puntuaciones predichas por el modelo como un gráfico de contornos
x = np.linspace(-20.0, 30.0)
y = np.linspace(-20.0, 40.0)
X, Y = np.meshgrid(x, y)
XX = np.array([X.ravel(), Y.ravel()]).T
Z = -clf.score_samples(XX)
Z = Z.reshape(X.shape)

CS = plt.contour(
    X, Y, Z, norm=LogNorm(vmin=1.0, vmax=1000.0), levels=np.logspace(0, 3, 10)
)
CB = plt.colorbar(CS, shrink=0.8, extend="both")
plt.scatter(X_train[:, 0], X_train[:, 1], 0.8)

plt.title("Density Estimation with Gaussian Mixture Models")
plt.axis("tight")
plt.show()
```
