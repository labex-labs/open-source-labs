# Zeige die rechte y-Achse der ersten Parasitenachse

Wir zeigen die rechte y-Achse der ersten Parasitenachse mit der `par1.axis["right"].set_visible(True)`-Methode. Wir setzen auch `par1.axis["right"].major_ticklabels.set_visible(True)` und `par1.axis["right"].label.set_visible(True)`, um die Striche und die Bezeichnung der rechten y-Achse anzuzeigen.

```python
par1.axis["right"].set_visible(True)
par1.axis["right"].major_ticklabels.set_visible(True)
par1.axis["right"].label.set_visible(True)
```
