# Analyse eines Bag-of-Words-Dokumentklassifizierers

Wir werden nun einen Klassifizierer zweimal trainieren, einmal auf den Textdaten einschließlich der Metadaten und einmal nach Entfernung der Metadaten. Wir werden die Klassifizierungsfehler auf einem Testset mithilfe einer Konfusionsmatrix analysieren und die Koeffizienten untersuchen, die die Klassifizierungsfunktion der trainierten Modelle definieren.

```python
from sklearn.linear_model import RidgeClassifier
from sklearn.metrics import ConfusionMatrixDisplay
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

clf = RidgeClassifier(tol=1e-2, solver="sparse_cg")
clf.fit(X_train, y_train)
pred = clf.predict(X_test)

fig, ax = plt.subplots(figsize=(10, 5))
ConfusionMatrixDisplay.from_predictions(y_test, pred, ax=ax)
ax.xaxis.set_ticklabels(target_names)
ax.yaxis.set_ticklabels(target_names)
_ = ax.set_title(
    f"Konfusionsmatrix für {clf.__class__.__name__}\nauf den ursprünglichen Dokumenten"
)

def plot_feature_effects():
    # gelernt Koeffizienten, gewichtet mit Häufigkeit des Auftretens
    average_feature_effects = clf.coef_ * np.asarray(X_train.mean(axis=0)).ravel()

    for i, label in enumerate(target_names):
        top5 = np.argsort(average_feature_effects[i])[-5:][::-1]
        if i == 0:
            top = pd.DataFrame(feature_names[top5], columns=[label])
            top_indices = top5
        else:
            top[label] = feature_names[top5]
            top_indices = np.concatenate((top_indices, top5), axis=None)
    top_indices = np.unique(top_indices)
    predictive_words = feature_names[top_indices]

    # Plotten der Feature-Effekte
    bar_size = 0.25
    padding = 0.75
    y_locs = np.arange(len(top_indices)) * (4 * bar_size + padding)

    fig, ax = plt.subplots(figsize=(10, 8))
    for i, label in enumerate(target_names):
        ax.barh(
            y_locs + (i - 2) * bar_size,
            average_feature_effects[i, top_indices],
            height=bar_size,
            label=label,
        )
    ax.set(
        yticks=y_locs,
        yticklabels=predictive_words,
        ylim=[
            0 - 4 * bar_size,
            len(top_indices) * (4 * bar_size + padding) - 4 * bar_size,
        ],
    )
    ax.legend(loc="lower right")

    print("top 5 Schlüsselwörter pro Klasse:")
    print(top)

    return ax

_ = plot_feature_effects().set_title("Durchschnittlicher Feature-Effekt auf die ursprünglichen Daten")
```
