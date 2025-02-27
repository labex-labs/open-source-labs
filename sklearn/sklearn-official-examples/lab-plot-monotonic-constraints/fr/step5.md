# Afficher la dépendance partielle

Nous allons maintenant afficher la dépendance partielle des prédictions par rapport aux deux caractéristiques pour les deux modèles.

```python
fig, ax = plt.subplots()
disp = PartialDependenceDisplay.from_estimator(
    gbdt_no_cst,
    X,
    features=[0, 1],
    feature_names=(
        "Première caractéristique",
        "Deuxième caractéristique",
    ),
    line_kw={"linewidth": 4, "label": "non contraint", "color": "tab:blue"},
    ax=ax,
)
PartialDependenceDisplay.from_estimator(
    gbdt_with_monotonic_cst,
    X,
    features=[0, 1],
    line_kw={"linewidth": 4, "label": "contraint", "color": "tab:orange"},
    ax=disp.axes_,
)

for f_idx in (0, 1):
    disp.axes_[0, f_idx].plot(
        X[:, f_idx], y, "o", alpha=0.3, zorder=-1, color="tab:green"
    )
    disp.axes_[0, f_idx].set_ylim(-6, 6)

plt.legend()
fig.suptitle("Effet des contraintes monotones sur les dépendances partielles")
plt.show()
```
