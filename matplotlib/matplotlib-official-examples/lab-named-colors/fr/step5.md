# Création d'un graphique en barres

Nous pouvons également utiliser Matplotlib pour créer un graphique en barres. Dans cet exemple, nous allons créer un graphique en barres qui montre le nombre de pommes, de bananes et d'oranges vendues.

```python
import matplotlib.pyplot as plt

# données à tracer
apples = 10
bananas = 15
oranges = 5

# création du graphique en barres
plt.bar(["Apples", "Bananas", "Oranges"], [apples, bananas, oranges])

# définition du titre
plt.title("Simple Bar Plot")

# définition de l'étiquette de l'axe x
plt.xlabel("Fruits")

# définition de l'étiquette de l'axe y
plt.ylabel("Quantité")

# affichage du graphique
plt.show()
```
