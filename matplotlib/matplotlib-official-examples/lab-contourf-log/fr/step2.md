# Générez l'ensemble de données

Nous allons générer un ensemble de données avec des valeurs positives et négatives en utilisant `numpy` :

```python
N = 100
x = np.linspace(-3.0, 3.0, N)
y = np.linspace(-2.0, 2.0, N)

X, Y = np.meshgrid(x, y)

# Une bosse basse avec une pointe sortante.
# Doit avoir l'axe z/couleur en échelle logarithmique, afin que nous voyions à la fois la bosse et la pointe.
# Une échelle linéaire ne montre que la pointe.
Z1 = np.exp(-X**2 - Y**2)
Z2 = np.exp(-(X * 10)**2 - (Y * 10)**2)
z = Z1 + 50 * Z2

# Mettez quelques valeurs négatives (coin inférieur gauche) pour causer des problèmes avec les logarithmes :
z[:5, :5] = -1

# Ce qui suit n'est pas strictement essentiel, mais cela éliminera
# un avertissement.  Commentez-le pour voir l'avertissement.
z = ma.masked_where(z <= 0, z)
```
