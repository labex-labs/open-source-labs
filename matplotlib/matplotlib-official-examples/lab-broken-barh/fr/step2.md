# Créez le graphique à barres horizontales brisées

Dans cette étape, nous allons créer le graphique à barres horizontales brisées. Nous utiliserons la méthode `broken_barh()` de la classe `Axes` pour créer le graphique. La méthode `broken_barh()` prend trois arguments : le premier argument est une liste de tuples où chaque tuple représente un segment de la barre et le premier élément du tuple est le point de départ du segment et le deuxième élément est la longueur du segment ; le deuxième argument est la coordonnée y de la barre ; et le troisième argument est la couleur de remplissage de la barre.

```python
fig, ax = plt.subplots()
ax.broken_barh([(110, 30), (150, 10)], (10, 9), facecolors='tab:blue')
ax.broken_barh([(10, 50), (100, 20), (130, 10)], (20, 9),
               facecolors=('tab:orange', 'tab:green', 'tab:red'))
ax.set_ylim(5, 35)
ax.set_xlim(0, 200)
ax.set_xlabel('seconds since start')
ax.set_yticks([15, 25], labels=['Bill', 'Jim'])
ax.grid(True)
ax.annotate('race interrupted', (61, 25),
            xytext=(0.8, 0.9), textcoords='axes fraction',
            arrowprops=dict(facecolor='black', shrink=0.05),
            fontsize=16,
            horizontalalignment='right', verticalalignment='top')

plt.show()
```
