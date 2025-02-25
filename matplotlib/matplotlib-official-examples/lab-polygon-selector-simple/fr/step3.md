# Créer un polygone de manière interactive

Pour créer un polygone de manière interactive, nous devons créer un objet `Figure` et un objet `Axes`. Ensuite, nous pouvons créer un objet `PolygonSelector` et y ajouter des sommets en cliquant sur le graphique. Nous pouvons également utiliser les touches `shift` et `ctrl` pour déplacer les sommets.

```python
fig, ax = plt.subplots()
selector = PolygonSelector(ax, lambda *args: None)

print("Cliquez sur la figure pour créer un polygone.")
print("Appuyez sur la touche 'échappement' pour commencer un nouveau polygone.")
print("Essayez de maintenir la touche 'Maj' pour déplacer tous les sommets.")
print("Essayez de maintenir la touche 'Ctrl' pour déplacer un seul sommet.")

plt.show()
```
