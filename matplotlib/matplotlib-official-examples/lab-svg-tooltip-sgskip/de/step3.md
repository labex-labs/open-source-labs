# Speichern der Abbildung als SVG

Wir speichern die Abbildung in einem gefälschten Dateiobjekt mithilfe der `BytesIO`-Klasse und der `savefig`-Methode.

```python
ax.set_xlim(-30, 30)
ax.set_ylim(-30, 30)
ax.set_aspect('equal')

f = BytesIO()
plt.savefig(f, format="svg")
```
