# Erstellen von zwei Histogrammen mit gestapelten Balken

Wir können zwei Histogramme mit gestapelten Balken erstellen, indem wir die `hist`-Funktion zweimal aufrufen und den `histtype`-Parameter auf `'barstacked'` setzen. In diesem Beispiel werden wir zwei Histogramme mit gestapelten Balken erstellen.

```python
plt.hist(x, density=True, histtype='barstacked', rwidth=0.8)
plt.hist(w, density=True, histtype='barstacked', rwidth=0.8)
plt.show()
```
