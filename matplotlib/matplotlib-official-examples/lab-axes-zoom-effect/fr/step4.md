# Connexion des axes

Dans cette étape, nous allons connecter les axes et créer l'effet de zoom. Nous allons créer une figure avec quatre axes et les connecter en utilisant les fonctions zoom_effect01 et zoom_effect02.

```python
axs = plt.figure().subplot_mosaic([
    ["zoom1", "zoom2"],
    ["main", "main"],
])

axs["main"].set(xlim=(0, 5))
zoom_effect01(axs["zoom1"], axs["main"], 0.2, 0.8)
axs["zoom2"].set(xlim=(2, 3))
zoom_effect02(axs["zoom2"], axs["main"])

plt.show()
```
