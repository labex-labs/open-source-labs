# Afficher les tailles de police

Enfin, nous allons afficher les différentes tailles de police disponibles dans Matplotlib. Nous utiliserons la méthode `fig.text()` pour afficher chaque taille de police, avec le nom de la taille comme texte et la taille de police correspondante comme argument clé.

```python
fig.text(0.9, 0.9,'size', **alignment)
sizes = [
    'xx-small', 'x-small','small','medium', 'large', 'x-large', 'xx-large']
for k, size in enumerate(sizes):
    fig.text(0.9, yp[k], size, size=size, **alignment)
```
