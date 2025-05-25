# Criando Dados para Plotagem

Nesta etapa, criaremos dados para plotar em um gráfico de contorno. Usamos a função `np.meshgrid()` para criar uma grade de pontos e, em seguida, calculamos os valores `z` usando as funções seno e cosseno.

```python
# Data to plot.
x, y = np.meshgrid(np.arange(7), np.arange(10))
z = np.sin(0.5 * x) * np.cos(0.52 * y)
```
