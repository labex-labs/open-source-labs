# Ergebnisse plotten

Schließlich können wir die Ergebnisse unserer Modelle plotten, um zu sehen, wie sie sich vergleichen. Wir werden die Unterstützung (d.h. den Ort der nicht-null-Koeffizienten) für jedes Modell sowie die Zeitreihe für ein Merkmal plotten.

```python
import matplotlib.pyplot as plt

fig = plt.figure(figsize=(8, 5))
plt.subplot(1, 2, 1)
plt.spy(coef_lasso_)
plt.xlabel("Merkmal")
plt.ylabel("Zeit (oder Aufgabe)")
plt.text(10, 5, "Lasso")
plt.subplot(1, 2, 2)
plt.spy(coef_multi_task_lasso_)
plt.xlabel("Merkmal")
plt.ylabel("Zeit (oder Aufgabe)")
plt.text(10, 5, "MultiTaskLasso")
fig.suptitle("Koeffizient Nicht-Null-Lage")

feature_to_plot = 0
plt.figure()
lw = 2
plt.plot(coef[:, feature_to_plot], color="seagreen", linewidth=lw, label="Wahrheit")
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
