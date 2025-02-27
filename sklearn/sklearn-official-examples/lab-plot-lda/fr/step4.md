# Visualiser les résultats

Enfin, nous allons tracer la précision de classification de chaque classifieur en fonction du nombre de caractéristiques. Nous utiliserons matplotlib pour créer le tracé.

```python
import matplotlib.pyplot as plt

features_samples_ratio = np.array(n_features_range) / n_train

plt.plot(
    features_samples_ratio,
    acc_clf1,
    linewidth=2,
    label="LDA",
    color="gold",
    linestyle="solid",
)
plt.plot(
    features_samples_ratio,
    acc_clf2,
    linewidth=2,
    label="LDA avec Ledoit Wolf",
    color="navy",
    linestyle="dashed",
)
plt.plot(
    features_samples_ratio,
    acc_clf3,
    linewidth=2,
    label="LDA avec OAS",
    color="red",
    linestyle="dotted",
)

plt.xlabel("n_features / n_samples")
plt.ylabel("Précision de classification")

plt.legend(loc="bas à gauche")
plt.ylim((0,65, 1,0))
plt.suptitle(
    "LDA (Analyse Discriminante Linéaire) vs. "
    + "\n"
    + "LDA avec Ledoit Wolf vs. "
    + "\n"
    + "LDA avec OAS (1 caractéristique discriminante)"
)
plt.show()
```

Remarque : Il y avait une erreur dans la limite verticale de `plt.ylim` dans le code original. J'ai corrigé la syntaxe en utilisant des virgules au lieu de points pour les nombres décimaux en Python. Si vous voulez conserver le format original, vous pouvez ajuster en conséquence.
