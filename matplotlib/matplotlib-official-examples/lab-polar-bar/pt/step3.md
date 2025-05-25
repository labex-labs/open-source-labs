# Definir os dados

Definiremos os dados para o gráfico. Geraremos 20 valores aleatórios para raios e ângulos.

```python
N = 20
theta = np.linspace(0.0, 2 * np.pi, N, endpoint=False)
radii = 10 * np.random.rand(N)
width = np.pi / 4 * np.random.rand(N)
colors = plt.cm.viridis(radii / 10.)
```
