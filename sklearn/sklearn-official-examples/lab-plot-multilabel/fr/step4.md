# Tracer les sous-graphiques

Dans cette étape, nous utilisons la fonction `plot_subfigure` pour tracer les sous-graphiques.

```python
plt.figure(figsize=(8, 6))

plot_subfigure(X, Y, 1, "Avec des échantillons non étiquetés + CCA", "cca")
plot_subfigure(X, Y, 2, "Avec des échantillons non étiquetés + PCA", "pca")

X, Y = make_multilabel_classification(
    n_classes=2, n_labels=1, allow_unlabeled=False, random_state=1
)

plot_subfigure(X, Y, 3, "Sans des échantillons non étiquetés + CCA", "cca")
plot_subfigure(X, Y, 4, "Sans des échantillons non étiquetés + PCA", "pca")

plt.subplots_adjust(0.04, 0.02, 0.97, 0.94, 0.09, 0.2)
plt.show()
```
