# Hinzufügen von Text zum Plot

Wir können Text zum Plot hinzufügen, indem wir die `text`-Funktion verwenden. Wir können die Position, die Rotation, die horizontale und vertikale Ausrichtung sowie die Mehrzeilenausrichtung des Texts angeben.

```python
ax0.text(2, 7, 'this is\nyet another test',
         rotation=45,
         horizontalalignment='center',
         verticalalignment='top',
         multialignment='center')
```
