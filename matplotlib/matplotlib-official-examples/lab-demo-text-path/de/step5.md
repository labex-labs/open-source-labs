# Erstellen einer verankerten Offset-Box

Erstellen Sie eine verankerte Offset-Box mit `AnnotationBbox`, um die Offset-Box hinzuzufügen und ihre Position festzulegen. Verwenden Sie den folgenden Code, um die verankerte Offset-Box zu erstellen:

```python
ao = AnchoredOffsetbox(loc='upper left', child=offsetbox, frameon=True,
                           borderpad=0.2)
ax1.add_artist(ao)
```
