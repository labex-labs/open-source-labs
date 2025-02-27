# Visualiser les résultats

Enfin, nous visualisons les résultats de nos modèles SVR en les traçant par rapport à l'ensemble de données d'échantillonnage. Nous traçons également les vecteurs de support et les autres données d'entraînement.

```python
import matplotlib.pyplot as plt

# Regarder les résultats
lw = 2

label_kernel = ["RBF", "Linéaire", "Polynômiale"]
couleur_modele = ["m", "c", "g"]

fig, axes = plt.subplots(nrows=1, ncols=3, figsize=(15, 10), sharey=True)

for ix, svr in enumerate(svrs):
    axes[ix].plot(
        X,
        svr.predict(X),
        color=couleur_modele[ix],
        lw=lw,
        label="Modèle {}".format(label_kernel[ix]),
    )
    axes[ix].scatter(
        X[svr.support_],
        y[svr.support_],
        facecolor="none",
        edgecolor=couleur_modele[ix],
        s=50,
        label="{} vecteurs de support".format(label_kernel[ix]),
    )
    axes[ix].scatter(
        X[np.setdiff1d(np.arange(len(X)), svr.support_)],
        y[np.setdiff1d(np.arange(len(X)), svr.support_)],
        facecolor="none",
        edgecolor="k",
        s=50,
        label="autres données d'entraînement",
    )
    axes[ix].legend(
        loc="upper center",
        bbox_to_anchor=(0.5, 1.1),
        ncol=1,
        fancybox=True,
        shadow=True,
    )

fig.text(0.5, 0.04, "données", ha="center", va="center")
fig.text(0.06, 0.5, "cible", ha="center", va="center", rotation="vertical")
fig.suptitle("Régression vectorielle support", fontsize=14)
plt.show()
```
