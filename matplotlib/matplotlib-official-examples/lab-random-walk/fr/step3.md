# Définition de la fonction de mise à jour

Nous définissons une fonction qui met à jour le graphique pour chaque trame de l'animation. La fonction prend trois entrées : `num` est le numéro de la trame actuelle, `walks` est une liste de tous les mouvements aléatoires et `lines` est une liste de toutes les lignes dans le graphique. Pour chaque ligne et mouvement, nous mettons à jour les données pour les coordonnées x, y et z de la ligne jusqu'au numéro de trame actuel. Nous utilisons `line.set_data()` et `line.set_3d_properties()` pour mettre à jour les coordonnées x-y et z respectivement.

```python
def update_lines(num, walks, lines):
    for line, walk in zip(lines, walks):
        # REMARQUE : il n'y a pas de.set_data() pour les données en 3 dimensions...
        line.set_data(walk[:num, :2].T)
        line.set_3d_properties(walk[:num, 2])
    return lines
```
