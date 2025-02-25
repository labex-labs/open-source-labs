# Erstellen der Figur und der Achsen

Wir werden das Figur- und Achsenobjekt mit der Funktion `subplots()` erstellen. Wir werden auch einen gelben Kreis-Patch zum Achsenobjekt mit der Funktion `patches.Circle()` hinzufügen.

```python
fig, ax = plt.subplots()
circ = patches.Circle((0.5, 0.5), 0.25, alpha=0.8, fc='yellow')
ax.add_patch(circ)
```
