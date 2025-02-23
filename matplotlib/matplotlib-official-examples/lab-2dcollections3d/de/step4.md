# Diagramm anpassen

Der vierte Schritt besteht darin, das Diagramm anzupassen, indem man eine Legende hinzufügt, die Achsengrenzen und -beschriftungen setzt und den Blickwinkel ändert.

```python
# Legende erstellen, Achsengrenzen und -beschriftungen setzen
ax.legend()
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.set_zlim(0, 1)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

# Den Blickwinkel anpassen, um更容易 zu erkennen, dass die Streupunkte
# in der Ebene y=0 liegen
ax.view_init(elev=20., azim=-35, roll=0)

plt.show()
```
