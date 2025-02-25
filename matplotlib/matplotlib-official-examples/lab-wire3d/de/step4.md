# Das Diagramm anpassen

Wir können das Diagramm anpassen, um es visuell ansprechender zu gestalten. In diesem Beispiel werden wir einen Titel, Achsenbeschriftungen hinzufügen und die Farbe des Diagramms ändern.

```python
# Customize the plot
ax.set_title('Wireframe Plot')
ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')
ax.plot_wireframe(X, Y, Z, rstride=5, cstride=5, color='green')
```
