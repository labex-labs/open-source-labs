# Festlegen der Achsengrenzen und Speichern der Figur

Wir legen die x- und y-Grenzen für die Achsen fest und speichern die Figur als Byte-String im SVG-Format mit `io.BytesIO()` und `plt.savefig()`.

```python
ax.set_xlim(0., 1.)
ax.set_ylim(0., 1.)

f = io.BytesIO()
plt.savefig(f, format="svg")
```
