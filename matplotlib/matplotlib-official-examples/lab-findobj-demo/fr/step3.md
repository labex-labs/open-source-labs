# Création d'un graphique simple

Le graphique le plus simple dans Matplotlib est un graphique en ligne. Vous pouvez créer un graphique en ligne à l'aide de la méthode `plot()`. Voici un exemple de code qui crée un graphique en ligne simple :

```python
import matplotlib.pyplot as plt

# Données
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

# Crée un graphique
plt.plot(x, y)

# Ajoute des étiquettes et un titre
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Simple Plot')

# Affiche le graphique
plt.show()
```

Dans ce code, nous définissons d'abord nos points de données comme deux listes `x` et `y`. Nous créons ensuite un graphique à l'aide de la méthode `plot()` et nous passons nos points de données. Nous ajoutons ensuite des étiquettes aux axes X et Y et un titre au graphique à l'aide des méthodes `xlabel()`, `ylabel()` et `title()`. Enfin, nous affichons le graphique à l'aide de la méthode `show()`.
