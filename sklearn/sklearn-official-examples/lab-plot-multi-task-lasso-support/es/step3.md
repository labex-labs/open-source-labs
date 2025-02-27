# Graficar resultados

Finalmente, podemos graficar los resultados de nuestros modelos para ver cómo se comparan. Graficaremos el soporte (es decir, la ubicación de los coeficientes no nulos) para cada modelo, así como la serie temporal de una de las características.

```python
import matplotlib.pyplot as plt

fig = plt.figure(figsize=(8, 5))
plt.subplot(1, 2, 1)
plt.spy(coef_lasso_)
plt.xlabel("Característica")
plt.ylabel("Tiempo (o Tarea)")
plt.text(10, 5, "Lasso")
plt.subplot(1, 2, 2)
plt.spy(coef_multi_task_lasso_)
plt.xlabel("Característica")
plt.ylabel("Tiempo (o Tarea)")
plt.text(10, 5, "MultiTaskLasso")
fig.suptitle("Ubicación no nula del coeficiente")

feature_to_plot = 0
plt.figure()
lw = 2
plt.plot(coef[:, feature_to_plot], color="seagreen", linewidth=lw, label="Verdad básica")
plt.plot(
    coef_lasso_[:, feature_to_plot], color="cornflowerblue", linewidth=lw, label="Lasso"
)
plt.plot(
    coef_multi_task_lasso_[:, feature_to_plot],
    color="gold",
    linewidth=lw,
    label="MultiTaskLasso",
)
plt.legend(loc="upper center")
plt.axis("tight")
plt.ylim([-1.1, 1.1])
plt.show()
```
