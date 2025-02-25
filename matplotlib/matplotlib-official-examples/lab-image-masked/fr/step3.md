# Personnalisation du graphique

Maintenant que nous avons créé un graphique de base, allons le personnaliser pour le rendre plus visuellement attrayant. Nous pouvons ajouter un titre, des étiquettes d'axe et changer la couleur et le style de la ligne.

```python
# Add title and axis labels
plt.title('Sin Wave')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')

# Change color and style of line
plt.plot(x, y, color='red', linestyle='dashed')
plt.show()
```
