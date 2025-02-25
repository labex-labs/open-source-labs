# Erzeuge den Konturplot

Wir werden nun den Konturplot mit der Methode `contourf()` erstellen. Diese Methode erstellt gefüllte Konturen. Wir werden den Parameter `cmap` auf `cm.coolwarm` setzen, um die cool-warm Farbpalette zu verwenden.

```python
ax.contourf(X, Y, Z, cmap=cm.coolwarm)
```
