# Linienplots erstellen

Wir werden Linienplots mit den zufälligen Daten erstellen, die wir im vorherigen Schritt generiert haben.

```python
# Generate line plots
lines = []
for i in range(len(data)):
    # Small reduction of the X extents to get a cheap perspective effect
    xscale = 1 - i / 200.
    # Same for linewidth (thicker strokes on bottom)
    lw = 1.5 - i / 100.0
    line, = ax.plot(xscale * X, i + G * data[i], color="w", lw=lw)
    lines.append(line)
```
