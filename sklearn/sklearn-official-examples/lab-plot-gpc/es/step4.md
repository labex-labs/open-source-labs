# Graficar las posteriores

Graficaremos las posteriores del modelo GPC utilizando hiperparámetros fijos y optimizados. Graficaremos los datos de entrenamiento, los datos de prueba y la probabilidad predicha de la clase 1. También etiquetaremos las gráficas.

```python
# Plot posteriors
plt.figure()
plt.scatter(X[:train_size, 0], y[:train_size], c="k", label="Train data", edgecolors=(0, 0, 0))
plt.scatter(X[train_size:, 0], y[train_size:], c="g", label="Test data", edgecolors=(0, 0, 0))
X_ = np.linspace(0, 5, 100)
plt.plot(X_, gp_fix.predict_proba(X_[:, np.newaxis])[:, 1], "r", label="Initial kernel: %s" % gp_fix.kernel_)
plt.plot(X_, gp_opt.predict_proba(X_[:, np.newaxis])[:, 1], "b", label="Optimized kernel: %s" % gp_opt.kernel_)
plt.xlabel("Feature")
plt.ylabel("Class 1 probability")
plt.xlim(0, 5)
plt.ylim(-0.25, 1.5)
plt.legend(loc="best")
```
