# Ein Balkendiagramm mit Schraffierung erstellen

Jetzt, wo du deine Daten hast, kannst du ein Balkendiagramm mit Schraffierung erstellen. Du kannst Schraffierungen verwenden, um Muster auf den Balken in deinem Diagramm zu erzeugen. In diesem Fall werden wir das `hatch`-Parameter verwenden, um Schraffierungen zu unseren Balken hinzuzufügen.

```python
plt.bar(x, y1, edgecolor='black', hatch="/")
plt.bar(x, y2, bottom=y1, edgecolor='black', hatch='//')
```
