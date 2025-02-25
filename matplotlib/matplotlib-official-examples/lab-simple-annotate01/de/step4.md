# Pfeilanmerkung hinzufügen

Wir werden nun einer Pfeilanmerkung zum Diagramm hinzufügen. Der folgende Code fügt einen Pfeil von der ersten Datenposition zur zweiten hinzu.

```python
ax.annotate("", xy=(1, 3), xytext=(2, 4),
            arrowprops=dict(arrowstyle="->", connectionstyle="arc3"))
```
