# Werte für das Streudiagramm berechnen

Wir werden die Werte für Delta1, Volumen und Schluss für das Streudiagramm berechnen.

```python
delta1 = np.diff(price_data.adj_close) / price_data.adj_close[:-1]

# Markergröße in Einheiten von Punkten^2
volume = (15 * price_data.volume[:-2] / price_data.volume[0])**2
close = 0.003 * price_data.close[:-2] / 0.003 * price_data.open[:-2]
```
