# Ergebnisse plotten und interpretieren

Der letzte Schritt besteht darin, die Ergebnisse zu plotten und zu interpretieren. Die Algorithmusleistung hängt davon ab, wie gut die True-Positive-Rate (TPR) bei einem niedrigen Wert der False-Positive-Rate (FPR) ist. Die besten Algorithmen haben die Kurve in der oberen linken Ecke des Plots und die Fläche unter der Kurve (AUC) nahe bei 1. Die diagonale durchgezogene Linie repräsentiert eine zufällige Klassifizierung von Ausreißern und Inlierern.

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

# Plotparameter
cols = 2
linewidth = 1
pos_label = 0  # Mittelwert 0 gehört zur positiven Klasse
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
plt.tight_layout(pad=2.0)  # Abstand zwischen den Teilplots
plt.show()
```
