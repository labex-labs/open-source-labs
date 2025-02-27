# Teilplots zeichnen

In diesem Schritt verwenden wir die Funktion `plot_subfigure`, um die Teilplots zu zeichnen.

```python
plt.figure(figsize=(8, 6))

plot_subfigure(X, Y, 1, "Mit unmarkierten Proben + CCA", "cca")
plot_subfigure(X, Y, 2, "Mit unmarkierten Proben + PCA", "pca")

X, Y = make_multilabel_classification(
    n_classes=2, n_labels=1, allow_unlabeled=False, random_state=1
)

plot_subfigure(X, Y, 3, "Ohne unmarkierte Proben + CCA", "cca")
plot_subfigure(X, Y, 4, "Ohne unmarkierte Proben + PCA", "pca")

plt.subplots_adjust(0.04, 0.02, 0.97, 0.94, 0.09, 0.2)
plt.show()
```
