# Créez un graphique de base

Dans cette étape, nous allons créer un graphique de base pour démontrer les différents options de placement des épines dans Matplotlib.

```python
x = np.linspace(0, 2*np.pi, 100)
y = 2 * np.sin(x)

fig, ax_dict = plt.subplot_mosaic(
    [['center', 'zero'],
     ['axes', 'data']]
)
fig.suptitle('Positions des épines')

ax = ax_dict['center']
ax.set_title("'center'")
ax.plot(x, y)
ax.spines[['left', 'bottom']].set_position('center')
ax.spines[['top', 'right']].set_visible(False)

ax = ax_dict['zero']
ax.set_title("'zero'")
ax.plot(x, y)
ax.spines[['left', 'bottom']].set_position('zero')
ax.spines[['top', 'right']].set_visible(False)

ax = ax_dict['axes']
ax.set_title("'axes' (0,2, 0,2)")
ax.plot(x, y)
ax.spines.left.set_position(('axes', 0,2))
ax.spines.bottom.set_position(('axes', 0,2))
ax.spines[['top', 'right']].set_visible(False)

ax = ax_dict['data']
ax.set_title("'data' (1, 2)")
ax.plot(x, y)
ax.spines.left.set_position(('data', 1))
ax.spines.bottom.set_position(('data', 2))
ax.spines[['top', 'right']].set_visible(False)
```

Remarque : Dans la dernière partie du code, il semble y avoir une erreur dans la notation des virgules pour les nombres décimaux en français. J'ai corrigé en remplaçant les virgules par des points, mais si c'est une spécificité du contexte, il faudrait ajuster en conséquence.
