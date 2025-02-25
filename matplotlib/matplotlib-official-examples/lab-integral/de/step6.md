# Füge das Integral-Label hinzu

Füge das Integral-Label zum Diagramm hinzu mit `text`. Das Label sollte in der Mitte zwischen a und b zentriert sein und mit Mathtext formatiert werden.

```python
ax.text(0.5 * (a + b), 30, r"$\int_a^b f(x)\mathrm{d}x$",
        horizontalalignment='center', fontsize=20)
```
