# Crear el menú

Ahora podemos crear el menú. Creamos una nueva figura y ajustamos el margen izquierdo. Luego creamos una lista de elementos del menú y los agregamos al menú. También definimos una función de devolución de llamada para cada elemento que imprimirá el elemento seleccionado.

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
