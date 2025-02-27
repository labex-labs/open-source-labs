# Tracez les limites de décision et les points d'entraînement

Dans cette étape, nous allons tracer les limites de décision et les points d'entraînement. Nous allons créer un objet `DecisionBoundaryDisplay` à l'aide de la méthode `from_estimator` du module `sklearn.inspection` et passer le classifieur AdaBoost, l'ensemble de données et d'autres paramètres. Nous allons également tracer les points d'entraînement en utilisant des couleurs différentes pour chaque classe.

```python
plot_colors = "br"
plot_step = 0.02
class_names = "AB"

plt.figure(figsize=(10, 5))

# Tracez les limites de décision
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

# Tracez les points d'entraînement
for i, n, c in zip(range(2), class_names, plot_colors):
    idx = np.where(y == i)
    plt.scatter(
        X[idx, 0],
        X[idx, 1],
        c=c,
        cmap=plt.cm.Paired,
        s=20,
        edgecolor="k",
        label="Class %s" % n,
    )
plt.xlim(x_min, x_max)
plt.ylim(y_min, y_max)
plt.legend(loc="upper right")

plt.title("Decision Boundary")
```
