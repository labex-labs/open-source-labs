# Créer un tracé à échelle personnalisée

Le dernier type de transformation d'échelle que nous allons explorer est la personnalisée. Cela nous permet de définir nos propres fonctions pour la transformation d'échelle, à la fois pour la fonction directe et la fonction inverse. Dans cet exemple, nous allons définir une fonction personnalisée pour prendre la racine carrée des données. Pour créer un tracé à échelle personnalisée, nous utilisons la méthode `set_yscale()` et nous passons la chaîne de caractères `'function'`. Nous définissons également les fonctions `forward()` et `inverse()` et nous les passons en tant qu'arguments au paramètre `functions`. Nous ajoutons également un titre et une grille au tracé.

```python
# Fonction x**(1/2)
def forward(x):
    return x**(1/2)

def inverse(x):
    return x**2

plt.plot(x, y)
plt.yscale('function', functions=(forward, inverse))
plt.title('Échelle personnalisée')
plt.grid(True)
```
