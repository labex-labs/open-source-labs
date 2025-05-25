# Gerar dados aleatórios

Geraremos dados aleatórios para o gráfico de dispersão usando NumPy. Criaremos 150 pontos de dados com valores aleatórios de raio e ângulo, e calcularemos a área e a cor de cada ponto.

```python
N = 150
r = 2 * np.random.rand(N)
theta = 2 * np.pi * np.random.rand(N)
area = 200 * r**2
colors = theta
```
