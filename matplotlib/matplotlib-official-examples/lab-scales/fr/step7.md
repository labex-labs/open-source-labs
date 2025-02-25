# Créer un tracé à l'échelle de la transformation de Mercator

En prime, nous allons également créer un tracé en utilisant la fonction de transformation de Mercator. Ce n'est pas une fonction intégrée dans Matplotlib, mais nous pouvons définir nos propres fonctions pour la fonction directe et la fonction inverse pour créer un tracé à l'échelle de la transformation de Mercator. Dans cet exemple, nous allons définir les fonctions `forward()` et `inverse()` pour la transformation de Mercator. Nous ajoutons également un titre et une grille au tracé.

```python
# Fonction de transformation de Mercator
def forward(a):
    a = np.deg2rad(a)
    return np.rad2deg(np.log(np.abs(np.tan(a) + 1.0 / np.cos(a))))

def inverse(a):
    a = np.deg2rad(a)
    return np.rad2deg(np.arctan(np.sinh(a)))

t = np.arange(0, 170.0, 0.1)
s = t / 2.

plt.plot(t, s, '-', lw=2)
plt.yscale('function', functions=(forward, inverse))
plt.title('Échelle de la transformation de Mercator')
plt.grid(True)
plt.xlim([0, 180])
```
