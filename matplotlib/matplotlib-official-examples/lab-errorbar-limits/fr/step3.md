# Créer un tracé simple de barre d'erreur

Nous allons créer un tracé simple de barre d'erreur avec des barre d'erreur standard à l'aide de la fonction `errorbar`. Ici, nous allons définir les valeurs de x et de y ainsi que leurs valeurs d'erreur correspondantes. Nous allons également définir le style de ligne en pointillé.

```python
fig, ax = plt.subplots(figsize=(7, 4))

# barre d'erreur standard
ax.errorbar(x, y, xerr=xerr, yerr=yerr, linestyle='dotted')
```
