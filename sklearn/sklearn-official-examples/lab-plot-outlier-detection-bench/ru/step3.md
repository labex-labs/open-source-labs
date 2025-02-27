# Построение и интерпретация результатов

Последним шагом является построение и интерпретация результатов. Производительность алгоритма зависит от того, насколько высокая точность обнаружения положительных объектов (TPR) при низком значении ложноположительного обнаружения (FPR). Лучшие алгоритмы имеют кривую в верхнем левом углу графика, а площадь под кривой (AUC) близка к 1. Диагональная пунктирная линия представляет случайную классификацию выбросов и нормальных объектов.

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

# параметры построения графика
cols = 2
linewidth = 1
pos_label = 0  # означает, что 0 относится к положительному классу
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
plt.tight_layout(pad=2.0)  # расстояние между подграфиками
plt.show()
```
