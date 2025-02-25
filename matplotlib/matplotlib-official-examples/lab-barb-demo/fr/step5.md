# Créer un graphique de flèches de vent masqué

Nous pouvons également créer un graphique de flèches de vent masqué en utilisant un tableau masqué. Dans ce cas, nous allons modifier la valeur d'un vecteur en une valeur incorrecte et la masquer.

```python
masked_u = np.ma.masked_array(U)
masked_u[4] = 1000  # Valeur incorrecte qui ne devrait pas être tracée lorsqu'elle est masquée
masked_u[4] = np.ma.masked

plt.barbs(X, Y, masked_u, V, length=8, pivot='middle')
plt.show()
```
