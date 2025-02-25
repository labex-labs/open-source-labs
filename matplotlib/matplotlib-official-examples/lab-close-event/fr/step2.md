# Créer une figure et connecter l'événement de fermeture

Dans cette étape, nous allons créer une figure et connecter l'événement de fermeture à la fonction `on_close` définie dans l'étape 1. Cela se fait en utilisant la méthode `mpl_connect` du canevas de la figure.

```python
fig = plt.figure()
fig.canvas.mpl_connect('close_event', on_close)
```
