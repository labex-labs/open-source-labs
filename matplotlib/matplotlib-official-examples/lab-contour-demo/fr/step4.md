# Placer manuellement les étiquettes des courbes de niveau

Nous pouvons également placer manuellement les étiquettes des courbes de niveau en fournissant une liste de positions (en coordonnées de données).

```python
fig, ax = plt.subplots()
CS = ax.contour(X, Y, Z)
manual_locations = [
    (-1, -1.4), (-0.62, -0.7), (-2, 0.5), (1.7, 1.2), (2.0, 1.4), (2.4, 1.7)]
ax.clabel(CS, inline=True, fontsize=10, manual=manual_locations)
ax.set_title('labels at selected locations')
```
