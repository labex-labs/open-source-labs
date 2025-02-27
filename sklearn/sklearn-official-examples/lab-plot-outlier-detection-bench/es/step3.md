# Graficar e interpretar los resultados

El último paso es graficar e interpretar los resultados. El rendimiento del algoritmo está relacionado con lo bien que se desempeña la tasa de verdaderos positivos (TPR) a un bajo valor de la tasa de falsos positivos (FPR). Los mejores algoritmos tienen la curva en la esquina superior izquierda de la gráfica y el área bajo la curva (AUC) cercana a 1. La línea discontinua diagonal representa una clasificación aleatoria de valores atípicos y valores normales.

```python
import math
import matplotlib.pyplot as plt
from sklearn.metrics import RocCurveDisplay

datasets_name = [
    "http",
    "smtp",
    "SA",
    "SF",
    "forestcover",
    "glass",
    "wdbc",
    "cardiotocography",
]

models_name = [
    "LOF",
    "IForest",
]

# parámetros de la gráfica
cols = 2
linewidth = 1
pos_label = 0  # significa que 0 pertenece a la clase positiva
rows = math.ceil(len(datasets_name) / cols)

fig, axs = plt.subplots(rows, cols, figsize=(10, rows * 3), sharex=True, sharey=True)

for i, dataset_name in enumerate(datasets_name):
    (X, y) = preprocess_dataset(dataset_name=dataset_name)

    for model_idx, model_name in enumerate(models_name):
        y_pred = compute_prediction(X, model_name=model_name)
        display = RocCurveDisplay.from_predictions(
            y,
            y_pred,
            pos_label=pos_label,
            name=model_name,
            linewidth=linewidth,
            ax=axs[i // cols, i % cols],
            plot_chance_level=(model_idx == len(models_name) - 1),
            chance_level_kw={
                "linewidth": linewidth,
                "linestyle": ":",
            },
        )
    axs[i // cols, i % cols].set_title(dataset_name)
plt.tight_layout(pad=2.0)  # espaciado entre los subgráficos
plt.show()
```
