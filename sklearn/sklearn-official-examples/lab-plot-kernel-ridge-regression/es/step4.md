# Observe los resultados

Visualizaremos el modelo aprendido de KRR y SVR cuando se optimizan tanto la complejidad/regularización como la anchura de banda del kernel RBF mediante búsqueda en cuadrícula.

```python
import matplotlib.pyplot as plt

sv_ind = svr.best_estimator_.support_
plt.scatter(
    X[sv_ind],
    y[sv_ind],
    c="r",
    s=50,
    label="Vectores de soporte de SVR",
    zorder=2,
    edgecolors=(0, 0, 0),
)
plt.scatter(X[:100], y[:100], c="k", label="datos", zorder=1, edgecolors=(0, 0, 0))
plt.plot(
    X_plot,
    y_svr,
    c="r",
    label="SVR (ajuste: %.3fs, predicción: %.3fs)" % (svr_fit, svr_predict),
)
plt.plot(
    X_plot, y_kr, c="g", label="KRR (ajuste: %.3fs, predicción: %.3fs)" % (kr_fit, kr_predict)
)
plt.xlabel("datos")
plt.ylabel("objetivo")
plt.title("SVR versus Ridge Kernel")
_ = plt.legend()
```
