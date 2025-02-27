# Graficar los resultados

Graficamos la verosimilitud de datos no vistos para diferentes valores del parámetro de encogimiento y mostramos las elecciones mediante validación cruzada, estimaciones de LedoitWolf y OAS.

```python
import matplotlib.pyplot as plt

fig = plt.figure()
plt.title("Covarianza regularizada: verosimilitud y coeficiente de encogimiento")
plt.xlabel("Parámetro de regularización: coeficiente de encogimiento")
plt.ylabel("Error: log-verosimilitud negativa en los datos de prueba")

plt.loglog(shrinkages, negative_logliks, label="Log-verosimilitud negativa")

plt.plot(plt.xlim(), 2 * [loglik_real], "--r", label="Verosimilitud de la covarianza real")

lik_max = np.amax(negative_logliks)
lik_min = np.amin(negative_logliks)
ymin = lik_min - 6.0 * np.log((plt.ylim()[1] - plt.ylim()[0]))
ymax = lik_max + 10.0 * np.log(lik_max - lik_min)
xmin = shrinkages[0]
xmax = shrinkages[-1]

plt.vlines(
    lw.shrinkage_,
    ymin,
    -loglik_lw,
    color="magenta",
    linewidth=3,
    label="Estimación de Ledoit-Wolf",
)

plt.vlines(
    oa.shrinkage_, ymin, -loglik_oa, color="purple", linewidth=3, label="Estimación de OAS"
)

plt.vlines(
    cv.best_estimator_.shrinkage,
    ymin,
    -cv.best_estimator_.score(X_test),
    color="cyan",
    linewidth=3,
    label="Mejor estimación por validación cruzada",
)

plt.ylim(ymin, ymax)
plt.xlim(xmin, xmax)
plt.legend()

plt.show()
```
