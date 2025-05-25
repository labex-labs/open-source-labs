# Plotar os Dados

Nesta etapa, plotaremos os dados no objeto eixos usando a função `plot` do Matplotlib. Plotaremos seis linhas diferentes com diferentes inclinações (declives) e ruído aleatório.

```python
ax.plot(x, np.sin(x) + x + noise)
ax.plot(x, np.sin(x) + 0.5 * x + noise)
ax.plot(x, np.sin(x) + 2 * x + noise)
ax.plot(x, np.sin(x) - 0.5 * x + noise)
ax.plot(x, np.sin(x) - 2 * x + noise)
ax.plot(x, np.sin(x) + noise)
```
