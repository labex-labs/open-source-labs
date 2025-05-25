# Adicionar uma linha de melhor ajuste

Nesta etapa, adicionaremos uma linha de melhor ajuste ao histograma. Calcularemos os valores y para a linha e a plotaremos sobre o histograma.

```python
y = ((1 / (np.sqrt(2 * np.pi) * sigma)) *
     np.exp(-0.5 * (1 / sigma * (bins - mu))**2))
ax.plot(bins, y, '--')
```
