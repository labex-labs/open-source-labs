# Plotar e Interpretar Resultados

O passo final é plotar e interpretar os resultados. O desempenho do algoritmo está relacionado à qualidade da taxa de verdadeiros positivos (TPR) em valores baixos da taxa de falsos positivos (FPR). Os melhores algoritmos têm a curva no canto superior esquerdo do gráfico e a área sob a curva (AUC) próxima de 1. A linha tracejada diagonal representa uma classificação aleatória de valores discrepantes e valores internos.

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

# parâmetros de plotagem
cols = 2
linewidth = 1
pos_label = 0  # significa que 0 pertence à classe positiva
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
plt.tight_layout(pad=2.0)  # espaçamento entre os subgráficos
plt.show()
```
