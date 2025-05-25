# Gerar Dados

Nesta etapa, geraremos os dados para o gráfico de linha. Usaremos a função `arange()` do NumPy para gerar um array de valores para o eixo x, e a função `sin()` para gerar um array de valores do eixo y para uma onda senoidal.

```python
x = np.arange(0, 2*np.pi, 0.01)
line, = ax.plot(x, np.sin(x))
```
