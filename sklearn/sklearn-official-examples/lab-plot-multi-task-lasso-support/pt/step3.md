# Plotar Resultados

Finalmente, podemos plotar os resultados de nossos modelos para comparar como eles se comportam. Plotaremos o suporte (ou seja, a localização dos coeficientes não nulos) para cada modelo, bem como a série temporal para uma das características.

```python
import matplotlib.pyplot as plt

fig = plt.figure(figsize=(8, 5))
plt.subplot(1, 2, 1)
plt.spy(coef_lasso_)
plt.xlabel("Característica")
plt.ylabel("Tempo (ou Tarefa)")
plt.text(10, 5, "Lasso")
plt.subplot(1, 2, 2)
plt.spy(coef_multi_task_lasso_)
plt.xlabel("Característica")
plt.ylabel("Tempo (ou Tarefa)")
plt.text(10, 5, "MultiTaskLasso")
fig.suptitle("Localização de coeficientes não nulos")

feature_to_plot = 0
plt.figure()
lw = 2
plt.plot(coef[:, feature_to_plot], color="seagreen", linewidth=lw, label="Verdade fundamental")
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
