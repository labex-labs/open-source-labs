# Configurez l'écrivain

Nous devons configurer l'écrivain qui sera utilisé pour enregistrer les images dans un fichier. Nous définissons le nombre d'images par seconde (fps) et ajoutons des métadonnées telles que le titre, l'artiste et le commentaire.

```python
metadata = dict(title='Movie Test', artist='Matplotlib',
                comment='Movie support!')
writer = FFMpegWriter(fps=15, metadata=metadata)
```
