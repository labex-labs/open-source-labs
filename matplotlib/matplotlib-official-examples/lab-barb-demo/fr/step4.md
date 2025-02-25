# Personnaliser le graphique de flèches de vent

Nous pouvons personnaliser le graphique de flèches de vent en changeant les paramètres de la fonction barbs. Par exemple, nous pouvons modifier la longueur et le point de pivot des vecteurs, remplir les cercles pour une flèche vide et changer les couleurs des drapeaux et des barres.

```python
plt.barbs(X, Y, U, V, length=8, pivot='middle', fill_empty=True, rounding=False,
          sizes=dict(emptybarb=0.25, spacing=0.2, height=0.3), flagcolor='r',
          barbcolor=['b', 'g'], flip_barb=True, barb_increments=dict(half=10, full=20, flag=100))
plt.show()
```
