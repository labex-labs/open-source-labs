# Daten mit \frac plotten

Wir werden die Daten mit dem \frac-TeX-Makro plotten und das resultierende Diagramm anzeigen.

```python
ax.plot(x, y, label=r'$\frac{sin(x)}{x}$')
ax.legend()
plt.show()
```
