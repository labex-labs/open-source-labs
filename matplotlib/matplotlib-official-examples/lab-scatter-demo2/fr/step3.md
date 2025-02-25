# Calculer les valeurs pour le graphique en nuage de points

Nous allons calculer les valeurs de delta1, volume et close pour le graphique en nuage de points.

```python
delta1 = np.diff(price_data.adj_close) / price_data.adj_close[:-1]

# Taille du marqueur en unités de points^2
volume = (15 * price_data.volume[:-2] / price_data.volume[0])**2
close = 0.003 * price_data.close[:-2] / 0.003 * price_data.open[:-2]
```
