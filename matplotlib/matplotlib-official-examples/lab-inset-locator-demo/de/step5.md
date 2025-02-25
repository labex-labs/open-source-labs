# Erstellen von Einfügebereichen mit beliebigen Positionen

Wir können Einfügebereiche mit beliebigen Positionen erstellen, indem wir den Parameter `bbox_to_anchor` verwenden, um eine Begrenzungsbox in Datenkoordinaten anzugeben, und den Parameter `bbox_transform` verwenden, um die Transformation für die Begrenzungsbox anzugeben.

```python
# Erstellen Sie einen Einfügebereich in Datenkoordinaten, indem Sie ax.transData als Transformation verwenden
axins3 = inset_axes(ax2, width="100%", height="100%",
                    bbox_to_anchor=(1e-2, 2, 1e3, 3),
                    bbox_transform=ax2.transData, loc=2, borderpad=0)
```
