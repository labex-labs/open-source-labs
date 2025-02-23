# Personnaliser le tracé

La quatrième étape consiste à personnaliser le tracé en ajoutant une légende, en définissant les limites et les étiquettes des axes, et en changeant l'angle de vue.

```python
# Créer une légende, définir les limites et les étiquettes des axes
ax.legend()
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.set_zlim(0, 1)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

# Personnaliser l'angle de vue pour qu'il soit plus facile de voir que les points de dispersion
# se trouvent sur le plan y = 0
ax.view_init(elev=20., azim=-35, roll=0)

plt.show()
```
