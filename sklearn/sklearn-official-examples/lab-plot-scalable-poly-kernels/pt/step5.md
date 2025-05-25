# Comparar os Resultados

Plotaremos os resultados dos diferentes métodos contra seus tempos de treinamento para comparar seu desempenho.

```python
import matplotlib.pyplot as plt

# Plotar os resultados dos diferentes métodos
fig, ax = plt.subplots(figsize=(7, 7))
ax.scatter(
    [
        lsvm_time,
    ],
    [
        lsvm_score,
    ],
    label="SVM Linear",
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
    label="SVM Kernel",
    c="red",
    marker="x",
)

ax.set_xlabel("Tempo de treinamento (s)")
ax.set_ylabel("Precisão (%)")
ax.legend()
plt.show()
```
