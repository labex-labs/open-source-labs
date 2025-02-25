# Personnaliser le tracé

Nous pouvons personnaliser notre tracé en changeant la couleur de la grille et en ajoutant une légende. Dans cet exemple, nous déplacerons la légende légèrement loin du centre du tracé pour éviter tout chevauchement.

```python
ax.tick_params(grid_color="palegoldenrod")
angle = np.deg2rad(67.5)
ax.legend(loc="lower left",
          bbox_to_anchor=(.5 + np.cos(angle)/2,.5 + np.sin(angle)/2))
```
