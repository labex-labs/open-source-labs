# Personnaliser le graphique

Nous pouvons personnaliser le graphique en ajoutant des étiquettes d'axe et un titre. Nous pouvons également changer la couleur des étiquettes d'axe et du titre de la légende. Le code suivant montre comment personnaliser le graphique :

```python
fig, ax = plt.subplots()
ax.bar(fruits, counts, label=bar_labels, color=bar_colors)
ax.set_ylabel('fruit supply', color='blue')
ax.set_xlabel('fruit names', color='blue')
ax.set_title('Fruit supply by kind and color', color='purple')
ax.legend(title='Fruit color', title_color='red', labelcolor='green')
plt.show()
```
