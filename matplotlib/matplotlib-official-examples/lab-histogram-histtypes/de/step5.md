# Ändern des Histogrammstils

Wir können den Stil des Histogramms ändern, indem wir den `histtype`-Parameter in der `hist`-Funktion angeben. In diesem Beispiel werden wir ein Histogramm mit einer Stufenkurve erstellen, die eine Farbfüllung hat.

```python
plt.hist(x, bins=20, density=True, histtype='stepfilled', facecolor='g', alpha=0.75)
plt.show()
```
