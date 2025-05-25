# Calcular valores para o gráfico de dispersão (scatter plot)

Calcularemos os valores delta1, volume e close para o gráfico de dispersão.

```python
delta1 = np.diff(price_data.adj_close) / price_data.adj_close[:-1]

# Marker size in units of points^2
volume = (15 * price_data.volume[:-2] / price_data.volume[0])**2
close = 0.003 * price_data.close[:-2] / 0.003 * price_data.open[:-2]
```
