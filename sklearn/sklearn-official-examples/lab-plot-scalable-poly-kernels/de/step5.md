# Die Ergebnisse vergleichen

Wir werden die Ergebnisse der verschiedenen Methoden gegen ihre Trainingszeiten aufzeichnen, um ihre Leistung zu vergleichen.

```python
import matplotlib.pyplot as plt

# Zeichne die Ergebnisse der verschiedenen Methoden
fig, ax = plt.subplots(figsize=(7, 7))
ax.scatter(
    [
        lsvm_time,
    ],
    [
        lsvm_score,
    ],
    label="Linear SVM",
    c="grün",
    marker="^",
)

for n_components in N_COMPONENTS:
    ax.scatter(
        [
            results[f"LSVM + PS({n_components})"]["time"],
        ],
        [
            results[f"LSVM + PS({n_components})"]["score"],
        ],
        c="blau",
    )
    ax.annotate(
        f"n_comp.={n_components}",
        (
            results[f"LSVM + PS({n_components})"]["time"],
            results[f"LSVM + PS({n_components})"]["score"],
        ),
        xytext=(-30, 10),
        textcoords="offset pixels",
    )

ax.scatter(
    [
        ksvm_time,
    ],
    [
        ksvm_score,
    ],
    label="Kernel SVM",
    c="rot",
    marker="x",
)

ax.set_xlabel("Trainingszeit (s)")
ax.set_ylabel("Genauigkeit (%)")
ax.legend()
plt.show()
```
