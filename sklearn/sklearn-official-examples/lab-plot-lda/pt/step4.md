# Visualizar Resultados

Finalmente, plotaremos a precisão da classificação para cada classificador em função do número de recursos. Usaremos matplotlib para criar o gráfico.

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
    label="LDA com Ledoit Wolf",
    color="navy",
    linestyle="dashed",
)
plt.plot(
    features_samples_ratio,
    acc_clf3,
    linewidth=2,
    label="LDA com OAS",
    color="red",
    linestyle="dotted",
)

plt.xlabel("n_features / n_samples")
plt.ylabel("Precisão da classificação")

plt.legend(loc="lower left")
plt.ylim((0.65, 1.0))
plt.suptitle(
    "LDA (Análise Discriminante Linear) vs. "
    + "\n"
    + "LDA com Ledoit Wolf vs. "
    + "\n"
    + "LDA com OAS (1 recurso discriminativo)"
)
plt.show()
```
