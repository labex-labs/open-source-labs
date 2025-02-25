# Création d'un graphique en barres

Nous allons créer un graphique en barres avec des valeurs de l'axe des x allant de 0 à 5 et les valeurs correspondantes de l'axe des y. Nous utiliserons la fonction `bar` fournie par le module `pyplot` pour créer le graphique en barres.

```python
# Création des valeurs de l'axe des x
x = np.arange(0, 5, 0.1)

# Création des valeurs de l'axe des y
y = np.sin(x)

# Création d'un graphique en barres
plt.bar(x, y)

# Ajout d'un titre et d'étiquettes au graphique
plt.title('Bar Plot')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')

# Affichage du graphique
plt.show()
```
