# Création d'un graphique de dispersion

Nous pouvons également utiliser Matplotlib pour créer un graphique de dispersion. Dans cet exemple, nous allons créer un graphique de dispersion qui montre la relation entre les valeurs de x et y.

```python
import matplotlib.pyplot as plt

# valeurs de l'axe x
x = [1, 2, 3, 4, 5]

# valeurs de l'axe y
y = [2, 4, 6, 8, 10]

# tracé des points
plt.scatter(x, y)

# définition du titre
plt.title("Simple Scatter Plot")

# définition de l'étiquette de l'axe x
plt.xlabel("X-axis")

# définition de l'étiquette de l'axe y
plt.ylabel("Y-axis")

# affichage du graphique
plt.show()
```
