# Ergebnisse visualisieren

Schließlich werden wir die Klassifizierungsgenauigkeit für jeden Klassifizierer als Funktion der Anzahl der Merkmale darstellen. Wir werden matplotlib verwenden, um das Diagramm zu erstellen.

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
plt.ylabel("Klassifizierungsgenauigkeit")

plt.legend(loc="lower left")
plt.ylim((0.65, 1.0))
plt.suptitle(
    "LDA (Lineare Diskriminanzanalyse) vs. "
    + "\n"
    + "LDA mit Ledoit Wolf vs. "
    + "\n"
    + "LDA mit OAS (1 diskriminierendes Merkmal)"
)
plt.show()
```
