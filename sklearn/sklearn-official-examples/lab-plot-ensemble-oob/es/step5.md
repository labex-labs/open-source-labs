# Visualizar la tasa de error OOB

Finalmente, graficaremos la tasa de error OOB para cada clasificador en función del número de estimadores. Esto nos permitirá identificar el número de estimadores en el que la tasa de error se estabiliza. Usaremos Matplotlib para generar la gráfica.

```python
for label, clf_err in error_rate.items():
    xs, ys = zip(*clf_err)
    plt.plot(xs, ys, label=label)

plt.xlim(min_estimators, max_estimators)
plt.xlabel("n_estimators")
plt.ylabel("Tasa de error OOB")
plt.legend(loc="upper right")
plt.show()
```
