# Trazar subgráficos

En este paso, utilizamos la función `plot_subfigure` para trazar los subgráficos.

```python
plt.figure(figsize=(8, 6))

plot_subfigure(X, Y, 1, "Con muestras sin etiquetar + CCA", "cca")
plot_subfigure(X, Y, 2, "Con muestras sin etiquetar + PCA", "pca")

X, Y = make_multilabel_classification(
    n_classes=2, n_labels=1, allow_unlabeled=False, random_state=1
)

plot_subfigure(X, Y, 3, "Sin muestras sin etiquetar + CCA", "cca")
plot_subfigure(X, Y, 4, "Sin muestras sin etiquetar + PCA", "pca")

plt.subplots_adjust(0.04, 0.02, 0.97, 0.94, 0.09, 0.2)
plt.show()
```
