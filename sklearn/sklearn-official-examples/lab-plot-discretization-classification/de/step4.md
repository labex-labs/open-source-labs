# Daten visualisieren

In diesem Schritt werden wir die synthetischen Klassifikationsdatensätze vor der Feature-Diskretisierung visualisieren. Wir werden die Trainings- und Testpunkte für jeden Datensatz plotten.

```python
fig, axes = plt.subplots(
    nrows=len(datasets), ncols=len(classifiers) + 1, figsize=(21, 9)
)

cm_piyg = plt.cm.PiYG
cm_bright = ListedColormap(["#b30065", "#178000"])

# iterieren über die Datensätze
for ds_cnt, (X, y) in enumerate(datasets):
    print(f"\ndataset {ds_cnt}\n---------")

    # in Trainings- und Testteil aufteilen
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.5, random_state=42
    )

    # das Gitter für die Hintergrundfarben erstellen
    x_min, x_max = X[:, 0].min() - 0.5, X[:, 0].max() + 0.5
    y_min, y_max = X[:, 1].min() - 0.5, X[:, 1].max() + 0.5
    xx, yy = np.meshgrid(np.arange(x_min, x_max, h), np.arange(y_min, y_max, h))

    # plotten Sie zunächst den Datensatz
    ax = axes[ds_cnt, 0]
    wenn ds_cnt == 0:
        ax.set_title("Eingabedaten")
    # plotten Sie die Trainingspunkte
    ax.scatter(X_train[:, 0], X_train[:, 1], c=y_train, cmap=cm_bright, edgecolors="k")
    # und Testpunkte
    ax.scatter(
        X_test[:, 0], X_test[:, 1], c=y_test, cmap=cm_bright, alpha=0.6, edgecolors="k"
    )
    ax.set_xlim(xx.min(), xx.max())
    ax.set_ylim(yy.min(), yy.max())
    ax.set_xticks(())
    ax.set_yticks(())
```
