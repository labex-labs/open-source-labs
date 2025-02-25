# Das Diagramm anpassen

Wir können das Diagramm anpassen, indem wir Beschriftungen für die x- und y-Achsen, einen Titel für das Diagramm und eine Legende hinzufügen. Wir können auch den Linienstil und die Farbe ändern.

```python
plt.plot(x, y, linestyle='--', color='red', label='sin(x)')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Line Plot')
plt.legend()
```
