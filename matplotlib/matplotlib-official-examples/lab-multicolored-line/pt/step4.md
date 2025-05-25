# Criar uma Norma Contínua

Criaremos uma norma contínua para mapear de pontos de dados para cores. Usaremos a função `Normalize` de `matplotlib.pyplot` para normalizar os valores de `dydx` entre seu mínimo e máximo. Em seguida, usaremos a função `LineCollection` para criar um conjunto de segmentos de linha e colori-los individualmente com base em sua derivada. Usaremos a função `set_array` para definir os valores usados para o colormapping.

```python
norm = plt.Normalize(dydx.min(), dydx.max())
lc = LineCollection(segments, cmap='viridis', norm=norm)
lc.set_array(dydx)
lc.set_linewidth(2)
```
