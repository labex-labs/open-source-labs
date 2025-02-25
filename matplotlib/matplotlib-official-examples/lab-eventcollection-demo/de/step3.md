# Die Daten sortieren

Um saubere Kurven zu erhalten, werden wir die Daten mit der `sort()`-Methode sortieren.

```python
# split the data into two parts
xdata1 = xdata[0, :]
xdata2 = xdata[1, :]
# sort the data so it makes clean curves
xdata1.sort()
xdata2.sort()
```
