# Erstellen von Einfügebereichen

Als nächstes werden wir in jedem der Unterdiagramme Einfügebereiche erstellen. Wir werden die `inset_axes()`-Methode verwenden, um die Einfügebereiche zu erstellen. Wir werden vier Einfügebereiche mit unterschiedlichen Größen und Positionen erstellen.

```python
from mpl_toolkits.axes_grid1.inset_locator import inset_axes

# Erstellen Sie einen Einfügebereich mit einer Breite von 1,3 Zoll und einer Höhe von 0,9 Zoll
# an der standardmäßigen oberen rechten Position
axins = inset_axes(ax, width=1.3, height=0.9)

# Erstellen Sie einen Einfügebereich mit einer Breite von 30% und einer Höhe von 40% der Begrenzung des übergeordneten Diagramms
# in der unteren linken Ecke (loc=3)
axins2 = inset_axes(ax, width="30%", height="40%", loc=3)

# Erstellen Sie einen Einfügebereich mit gemischten Spezifikationen im zweiten Unterdiagramm;
# Die Breite beträgt 30% der Begrenzung des übergeordneten Diagramms und
# Die Höhe beträgt 1 Zoll in der oberen linken Ecke (loc=2)
axins3 = inset_axes(ax2, width="30%", height=1., loc=2)

# Erstellen Sie einen Einfügebereich in der unteren rechten Ecke (loc=4) mit borderpad=1, d.h.
# 10 Punkte Abstand (da 10pt die standardmäßige Schriftgröße ist) zum übergeordneten Diagramm
axins4 = inset_axes(ax2, width="20%", height="20%", loc=4, borderpad=1)
```
