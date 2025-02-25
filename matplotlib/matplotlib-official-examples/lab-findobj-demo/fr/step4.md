# Personnalisation du graphique

Matplotlib propose un large éventail d'options de personnalisation pour les graphiques. Voici un exemple de code qui personnalise notre graphique en ligne simple :

```python
import matplotlib.pyplot as plt

# Données
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

# Crée un graphique
plt.plot(x, y, color='red', linewidth=2, linestyle='--', marker='o', markersize=8, markerfacecolor='yellow')

# Ajoute des étiquettes et un titre
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Customized Plot')

# Affiche le graphique
plt.show()
```

Dans ce code, nous utilisons divers paramètres de la méthode `plot()` pour personnaliser le graphique. Nous changeons la couleur de la ligne en rouge, la largeur de la ligne en 2, le style de ligne en pointillé (`--`), le marqueur en cercle (`o`), la taille du marqueur en 8 et la couleur de fond du marqueur en jaune.
