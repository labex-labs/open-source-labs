# Création du menu

Maintenant, nous pouvons créer le menu. Nous créons une nouvelle figure et ajustons la marge gauche. Ensuite, nous créons une liste d'éléments du menu et les ajoutons au menu. Nous définissons également une fonction de rappel pour chaque élément qui affichera l'élément sélectionné.

```python
fig = plt.figure()
fig.subplots_adjust(left=0.3)
props = ItemProperties(labelcolor='black', bgcolor='yellow',
                       fontsize=15, alpha=0.2)
hoverprops = ItemProperties(labelcolor='white', bgcolor='blue',
                            fontsize=15, alpha=0.2)

menuitems = []
for label in ('open', 'close','save','save as', 'quit'):
    def on_select(item):
        print('you selected %s' % item.labelstr)
    item = MenuItem(fig, label, props=props, hoverprops=hoverprops,
                    on_select=on_select)
    menuitems.append(item)

menu = Menu(fig, menuitems)
plt.show()
```
