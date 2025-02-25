# Création du graphique en barres avec les unités par défaut

Dans cette étape, nous allons créer le graphique en barres avec les unités par défaut à l'aide de la méthode `bar` de Matplotlib. Nous utiliserons le paramètre `bottom` pour définir le bas des barres à 0.

```python
fig, axs = plt.subplots(2, 2)

axs[0, 0].bar(cms, cms, bottom=bottom)
```
