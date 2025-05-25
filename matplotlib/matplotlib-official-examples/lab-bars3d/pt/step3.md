# Gerar Dados para os Gráficos de Barras

Agora, geraremos os dados para os gráficos de barras. Criaremos quatro conjuntos de dados, cada um com 20 valores. Usaremos o método `arange()` do NumPy para criar um array de 20 valores e o método `random.rand()` do NumPy para gerar valores aleatórios para cada conjunto de dados.

```python
colors = ['r', 'g', 'b', 'y']
yticks = [3, 2, 1, 0]
for c, k in zip(colors, yticks):
    xs = np.arange(20)
    ys = np.random.rand(20)
```
