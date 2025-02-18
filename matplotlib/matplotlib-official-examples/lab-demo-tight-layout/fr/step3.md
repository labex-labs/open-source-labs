# Personnalisation du graphique

Maintenant que nous avons un graphique de base, personnalisons-le.

```python
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

plt.plot(x, y, color='red', marker='o')
plt.title('My Plot')
plt.xlabel('X Axis Label')
plt.ylabel('Y Axis Label')
plt.show()
```

Ici, nous avons ajouté quelques personnalisations à notre graphique. Nous avons changé la couleur de la ligne en rouge et ajouté des marqueurs circulaires à chaque point de données. Nous avons également ajouté un titre et des étiquettes d'axe à notre graphique.
