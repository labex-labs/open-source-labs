# Visualizar los resultados

Finalmente, graficaremos la precisión de clasificación de cada clasificador en función del número de características. Utilizaremos matplotlib para crear la gráfica.

```python
import matplotlib.pyplot as plt

features_samples_ratio = np.array(n_features_range) / n_train

plt.plot(
    features_samples_ratio,
    acc_clf1,
    linewidth=2,
    label="LDA",
    color="gold",
    linestyle="solid",
)
plt.plot(
    features_samples_ratio,
    acc_clf2,
    linewidth=2,
    label="LDA with Ledoit Wolf",
    color="navy",
    linestyle="dashed",
)
plt.plot(
    features_samples_ratio,
    acc_clf3,
    linewidth=2,
    label="LDA with OAS",
    color="red",
    linestyle="dotted",
)

plt.xlabel("n_features / n_samples")
plt.ylabel("Precisión de clasificación")

plt.legend(loc="lower left")
plt.ylim((0.65, 1.0))
plt.suptitle(
    "LDA (Análisis Discriminante Lineal) vs. "
    + "\n"
    + "LDA con Ledoit Wolf vs. "
    + "\n"
    + "LDA con OAS (1 característica discriminativa)"
)
plt.show()
```
