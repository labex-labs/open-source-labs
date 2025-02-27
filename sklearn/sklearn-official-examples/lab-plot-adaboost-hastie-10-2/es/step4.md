# Graficar los resultados

Finalmente, graficamos los errores de entrenamiento y prueba de nuestras líneas base y de los clasificadores AdaBoost discreto y real.

```python
import matplotlib.pyplot as plt
import seaborn as sns

fig = plt.figure()
ax = fig.add_subplot(111)

ax.plot([1, n_estimators], [dt_stump_err] * 2, "k-", label="Error del Árbol de Decisión de Nodo Hoja")
ax.plot([1, n_estimators], [dt_err] * 2, "k--", label="Error del Árbol de Decisión")

colors = sns.color_palette("colorblind")

ax.plot(
    np.arange(n_estimators) + 1,
    ada_discrete_err,
    label="Error de Prueba de AdaBoost Discreto",
    color=colors[0],
)
ax.plot(
    np.arange(n_estimators) + 1,
    ada_discrete_err_train,
    label="Error de Entrenamiento de AdaBoost Discreto",
    color=colors[1],
)
ax.plot(
    np.arange(n_estimators) + 1,
    ada_real_err,
    label="Error de Prueba de AdaBoost Real",
    color=colors[2],
)
ax.plot(
    np.arange(n_estimators) + 1,
    ada_real_err_train,
    label="Error de Entrenamiento de AdaBoost Real",
    color=colors[4],
)

ax.set_ylim((0.0, 0.5))
ax.set_xlabel("Número de clasificadores débiles")
ax.set_ylabel("tasa de error")

leg = ax.legend(loc="upper right", fancybox=True)
leg.get_frame().set_alpha(0.7)

plt.show()
```
