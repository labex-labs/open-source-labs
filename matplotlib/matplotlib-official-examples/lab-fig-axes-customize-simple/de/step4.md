# Anpassen der Striche und Beschriftungen

Wir werden die Striche und Beschriftungen der Achsen mit der `ax1.tick_params()`-Methode anpassen. Wir werden die Farbe, die Rotation und die Größe der x-Achsenbeschriftung sowie die Farbe, die Größe und die Breite der y-Achsenstriche festlegen.

```python
ax1.tick_params(axis='x', labelcolor='tab:red', labelrotation=45, labelsize=16)
ax1.tick_params(axis='y', color='tab:green', size=25, width=3)
```
