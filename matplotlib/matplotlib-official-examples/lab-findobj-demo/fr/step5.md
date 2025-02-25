# Création de différents types de graphiques

Matplotlib prend en charge un large éventail de types de graphiques, y compris les graphiques en ligne, les graphiques de dispersion, les graphiques en barre, etc. Voici un exemple de code qui crée un graphique de dispersion :

```python
import matplotlib.pyplot as plt
import numpy as np

# Génère des données aléatoires
x = np.random.rand(50)
y = np.random.rand(50)
colors = np.random.rand(50)
sizes = 1000 * np.random.rand(50)

# Crée un graphique de dispersion
plt.scatter(x, y, c=colors, s=sizes, alpha=0.5)

# Ajoute des étiquettes et un titre
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Scatter Plot')

# Affiche le graphique
plt.show()
```

Dans ce code, nous utilisons la méthode `scatter()` pour créer un graphique de dispersion. Nous générons des données aléatoires à l'aide de la bibliothèque NumPy et nous la passons à la méthode `scatter()`. Nous utilisons également le paramètre `c` pour spécifier les couleurs des points de données, le paramètre `s` pour spécifier les tailles des points de données et le paramètre `alpha` pour spécifier la transparence des points de données.
