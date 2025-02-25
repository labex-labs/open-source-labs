# Création d'un graphique en ligne simple

Nous allons créer un graphique en ligne simple avec des valeurs de l'axe des x allant de 0 à 5 et les valeurs correspondantes de l'axe des y. Nous utiliserons la fonction `plot` fournie par le module `pyplot` pour créer le graphique en ligne.

```python
# Création des valeurs de l'axe des x
x = np.arange(0, 5, 0.1)

# Création des valeurs de l'axe des y
y = np.sin(x)

# Création d'un graphique en ligne
plt.plot(x, y)

# Ajout d'un titre et d'étiquettes au graphique
plt.title('Simple Line Plot')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')

# Affichage du graphique
plt.show()
```
