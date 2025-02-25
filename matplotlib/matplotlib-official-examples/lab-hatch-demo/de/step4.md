# Ein Balkendiagramm mit mehreren Schraffierungen erstellen

Du kannst auch mehrere Schraffierungen in deinem Balkendiagramm verwenden. In diesem Fall werden wir ein Array von Schraffierungen verwenden, um mehrere Schraffierungen auf unseren Balken zu erzeugen.

```python
plt.bar(x, y1, edgecolor='black', hatch=['--', '+', 'x', '\\'])
plt.bar(x, y2, bottom=y1, edgecolor='black', hatch=['*', 'o', 'O', '.'])
```
