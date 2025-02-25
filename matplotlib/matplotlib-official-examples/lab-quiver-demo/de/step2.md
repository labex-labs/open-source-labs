# Drehpunkt und Pfeilhäufigkeit

Die `quiver()`-Funktion kann auch verwendet werden, um den Drehpunkt der Pfeile und die Häufigkeit, mit der sie angezeigt werden, anzupassen. Der `pivot`-Parameter kann auf `'mid'` oder `'tip'` gesetzt werden, und die an `quiver()` übergebenen Arrays können abgeschnitten werden, um nur jeden n-ten Pfeil anzuzeigen.

```python
fig2, ax2 = plt.subplots()
ax2.set_title("pivot='mid'; every third arrow; units='inches'")
Q = ax2.quiver(X[::3, ::3], Y[::3, ::3], U[::3, ::3], V[::3, ::3],
               pivot='mid', units='inches')
qk = ax2.quiverkey(Q, 0.9, 0.9, 1, r'$1 \frac{m}{s}$', labelpos='E',
                   coordinates='figure')
ax2.scatter(X[::3, ::3], Y[::3, ::3], color='r', s=5)
plt.show()
```
