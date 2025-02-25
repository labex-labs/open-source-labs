# Erzeuge das Menü

Jetzt können wir das Menü erstellen. Wir erstellen eine neue Figur und passen den linken Rand an. Dann erstellen wir eine Liste von Menüelementen und fügen sie zum Menü hinzu. Wir definieren auch eine Callback-Funktion für jedes Element, die das ausgewählte Element ausdrucken wird.

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
