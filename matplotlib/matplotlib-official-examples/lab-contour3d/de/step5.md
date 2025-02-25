# Diagramm anpassen

Wir können das Diagramm anpassen, indem wir Beschriftungen für die Achsen hinzufügen und den Blickwinkel anpassen.

```python
ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')
ax.view_init(elev=30, azim=120)
```
