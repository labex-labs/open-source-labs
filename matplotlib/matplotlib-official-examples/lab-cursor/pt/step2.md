# Gerando Dados

Nesta etapa, geramos pontos de dados aleatórios usando numpy.

```python
# Fixing random state for reproducibility
np.random.seed(19680801)

# Generate random data points
x, y = 4*(np.random.rand(2, 100) - .5)
```
