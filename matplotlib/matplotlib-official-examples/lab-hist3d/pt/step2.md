# Gerar Dados

Em seguida, geraremos alguns dados 2D aleatórios para usar no histograma. Usaremos a função `random.rand()` do NumPy para gerar 100 valores aleatórios para as variáveis x e y.

```python
# Fixing random state for reproducibility
np.random.seed(19680801)

x, y = np.random.rand(2, 100) * 4
```
