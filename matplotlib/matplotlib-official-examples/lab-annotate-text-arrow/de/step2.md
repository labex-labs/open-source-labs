# Textanmerkungen zum Diagramm hinzufügen

Als nächstes fügen wir Textanmerkungen zum Diagramm hinzu, indem wir die Funktion `ax.text()` verwenden. Wir erstellen zwei Anmerkungen, eine für "Sample A" und eine für "Sample B".

```python
bbox_props = dict(boxstyle="round", fc="w", ec="0.5", alpha=0.9)
ax.text(-2, -2, "Sample A", ha="center", va="center", size=20,
        bbox=bbox_props)
ax.text(2, 2, "Sample B", ha="center", va="center", size=20,
        bbox=bbox_props)
```
