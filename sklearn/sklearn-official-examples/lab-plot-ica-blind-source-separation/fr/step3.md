# Tracer les résultats

Nous allons tracer le signal mixte original, les sources indépendantes d'origine, les sources estimées par l'ICA et les sources estimées par la PCA.

```python
import matplotlib.pyplot as plt

plt.figure()

models = [X, S, S_, H]
names = [
    "Observations (signal mixte)",
    "Véritables sources",
    "Signaux récupérés par l'ICA",
    "Signaux récupérés par la PCA",
]
couleurs = ["rouge", "bleu acier", "orange"]

Pour ii, (modèle, nom) dans enumerate(zip(models, names), 1):
    plt.subplot(4, 1, ii)
    plt.title(nom)
    Pour sig, couleur dans zip(model.T, couleurs):
        plt.plot(sig, couleur=couleur)

plt.tight_layout()
plt.show()
```
