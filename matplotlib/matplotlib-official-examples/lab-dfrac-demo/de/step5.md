# Daten mit \dfrac plotten

Wir werden die Daten mit dem \dfrac-TeX-Makro plotten und das resultierende Diagramm anzeigen.

```python
fig, ax = plt.subplots()
ax.plot(x, y, label=r'$\dfrac{sin(x)}{x}$')
ax.legend()
plt.show()
```
