# Tracer et interpréter les résultats

La dernière étape consiste à tracer et à interpréter les résultats. Les performances de l'algorithme dépendent de la qualité du taux de vrais positifs (TPR) pour de faibles valeurs du taux de faux positifs (FPR). Les meilleurs algorithmes ont une courbe dans le coin supérieur gauche du graphique et une aire sous la courbe (AUC) proche de 1. La ligne pointillée diagonale représente une classification aléatoire d'anomalies et de données normales.

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

# paramètres de tracé
cols = 2
linewidth = 1
pos_label = 0  # signifie que 0 appartient à la classe positive
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
plt.tight_layout(pad=2.0)  # espacement entre les sous-graphiques
plt.show()
```
