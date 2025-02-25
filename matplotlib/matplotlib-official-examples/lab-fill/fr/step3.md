# Générer un polygone rempli

Maintenant, nous pouvons générer un polygone rempli à l'aide de la fonction `fill()`. Nous allons utiliser la fonction du flocon de Koch pour générer les coordonnées du polygone.

```python
x, y = koch_snowflake(order=5)

plt.figure(figsize=(8, 8))
plt.axis('equal')
plt.fill(x, y)
plt.show()
```
