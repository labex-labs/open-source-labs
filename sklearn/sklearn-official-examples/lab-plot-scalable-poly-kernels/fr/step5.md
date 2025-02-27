# Comparer les résultats

Nous allons tracer les résultats des différentes méthodes en fonction de leurs temps d'entraînement pour comparer leurs performances.

```python
import matplotlib.pyplot as plt

# Tracer les résultats des différentes méthodes
fig, ax = plt.subplots(figsize=(7, 7))
ax.scatter(
    [
        lsvm_time,
    ],
    [
        lsvm_score,
    ],
    label="Linear SVM",
    c="green",
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
        c="blue",
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
    c="red",
    marker="x",
)

ax.set_xlabel("Temps d'entraînement (s)")
ax.set_ylabel("Précision (%)")
ax.legend()
plt.show()
```
