# Festlegen der Abbildung und der Achsen

Wir werden ein Figurenobjekt erstellen und vier Achsenobjekte mit der `fig.add_axes`-Methode einrichten.

```python
fig = plt.figure(figsize=(5.5, 4))
rect = (0.1, 0.1, 0.8, 0.8)
ax = [fig.add_axes(rect, label="%d" % i) for i in range(4)]
```
