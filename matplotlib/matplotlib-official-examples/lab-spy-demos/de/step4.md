# Plotten des Sparsamkeitmusters

Wir werden die `spy`-Funktion verwenden, um das Sparsamkeitmuster des Arrays zu plotten. Wir werden verschiedene Parameter wie `markersize` und `precision` verwenden, um den Plot anzupassen.

```python
ax1.spy(x, markersize=5)
ax2.spy(x, precision=0.1, markersize=5)
ax3.spy(x)
ax4.spy(x, precision=0.1)
```
