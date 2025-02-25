# Accéder à la barre d'outils et au conteneur vertical (VBox)

Nous allons accéder aux attributs de la barre d'outils et du conteneur vertical (VBox) du gestionnaire de canevas de la figure en utilisant respectivement les méthodes `manager.toolbar` et `manager.vbox`.

```python
manager = fig.canvas.manager
toolbar = manager.toolbar
vbox = manager.vbox
```
