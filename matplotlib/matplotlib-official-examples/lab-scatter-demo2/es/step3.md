# Calcular valores para el diagrama de dispersión

Calcularemos los valores de delta1, volumen y cierre para el diagrama de dispersión.

```python
delta1 = np.diff(price_data.adj_close) / price_data.adj_close[:-1]

# Tamaño del marcador en unidades de puntos^2
volume = (15 * price_data.volume[:-2] / price_data.volume[0])**2
close = 0.003 * price_data.close[:-2] / 0.003 * price_data.open[:-2]
```
