# Créer le graphique

Maintenant, nous allons créer le graphique en utilisant la fonction `subplots` de Matplotlib. Nous allons créer deux sous-graphiques, l'un pour les lignes verticales et l'autre pour les lignes horizontales. Nous définirons la taille de la figure sur (12, 6) pour une meilleure visibilité.

```python
# Create the plot
fig, (vax, hax) = plt.subplots(1, 2, figsize=(12, 6))
```
