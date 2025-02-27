# Die Entscheidungsgrenzen und die Trainingspunkte plotten

In diesem Schritt werden wir die Entscheidungsgrenzen und die Trainingspunkte plotten. Wir erstellen ein `DecisionBoundaryDisplay`-Objekt mithilfe der Methode `from_estimator` aus dem Modul `sklearn.inspection` und übergeben den AdaBoost-Klassifizierer, den Datensatz und andere Parameter. Wir plotten auch die Trainingspunkte mit unterschiedlichen Farben für jede Klasse.

```python
plot_colors = "br"
plot_step = 0.02
class_names = "AB"

plt.figure(figsize=(10, 5))

# Die Entscheidungsgrenzen plotten
ax = plt.subplot(121)
disp = DecisionBoundaryDisplay.from_estimator(
    bdt,
    X,
    cmap=plt.cm.Paired,
    response_method="predict",
    ax=ax,
    xlabel="x",
    ylabel="y",
)
x_min, x_max = disp.xx0.min(), disp.xx0.max()
y_min, y_max = disp.xx1.min(), disp.xx1.max()
plt.axis("tight")

# Die Trainingspunkte plotten
for i, n, c in zip(range(2), class_names, plot_colors):
    idx = np.where(y == i)
    plt.scatter(
        X[idx, 0],
        X[idx, 1],
        c=c,
        cmap=plt.cm.Paired,
        s=20,
        edgecolor="k",
        label="Klasse %s" % n,
    )
plt.xlim(x_min, x_max)
plt.ylim(y_min, y_max)
plt.legend(loc="upper right")

plt.title("Entscheidungsgrenze")
```
