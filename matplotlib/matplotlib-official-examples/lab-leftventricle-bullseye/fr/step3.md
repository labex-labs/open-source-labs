# Création d'un graphique de dispersion

Nous allons créer un graphique de dispersion avec des valeurs de l'axe des x allant de 0 à 5 et les valeurs correspondantes de l'axe des y. Nous utiliserons la fonction `scatter` fournie par le module `pyplot` pour créer le graphique de dispersion.

```python
# Création des valeurs de l'axe des x
x = np.arange(0, 5, 0.1)

# Création des valeurs de l'axe des y
y = np.sin(x)

# Création d'un graphique de dispersion
plt.scatter(x, y)

# Ajout d'un titre et d'étiquettes au graphique
plt.title('Scatter Plot')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')

# Affichage du graphique
plt.show()
```
