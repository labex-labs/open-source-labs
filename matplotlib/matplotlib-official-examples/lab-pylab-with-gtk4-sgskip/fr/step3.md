# Accédez à la barre d'outils et au conteneur vertical (vbox)

```python
manager = fig.canvas.manager
toolbar = manager.toolbar
vbox = manager.vbox
```

Nous accédons aux attributs `toolbar` et `vbox` du gestionnaire de la toile de la figure.
