# Konturplot erstellen

Wir werden nun den Konturplot mit der `contour()`-Funktion erstellen. Wir werden die `X`, `Y` und `Z`-Daten übergeben und `extend3d=True` setzen, um die Kurven vertikal zu 'Bändern' zu erweitern. Wir werden auch die Farbskala auf `cm.coolwarm` setzen, um ein schönes Farbschema zu erhalten.

```python
ax.contour(X, Y, Z, extend3d=True, cmap=cm.coolwarm)
```
