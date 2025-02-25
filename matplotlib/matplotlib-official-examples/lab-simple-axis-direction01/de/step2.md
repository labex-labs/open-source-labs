# Figur und Achsen erstellen

Als nächstes erstellen wir die Figur- und Achsenobjekte mit der Funktion `plt.subplots()`. Wir geben die Größe der Figur über den Parameter `figsize` an.

```python
fig = plt.figure(figsize=(4, 2.5))
ax1 = fig.add_subplot(axes_class=axisartist.Axes)
```
