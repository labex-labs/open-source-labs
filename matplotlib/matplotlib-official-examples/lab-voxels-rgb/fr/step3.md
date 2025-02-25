# Création de la sphère

Nous allons maintenant créer une sphère dans le graphique en définissant une condition pour les valeurs RGB qui se trouvent à une certaine distance du centre du graphique.

```python
rc = midpoints(r)
gc = midpoints(g)
bc = midpoints(b)

sphere = (rc - 0.5)**2 + (gc - 0.5)**2 + (bc - 0.5)**2 < 0.5**2
```
