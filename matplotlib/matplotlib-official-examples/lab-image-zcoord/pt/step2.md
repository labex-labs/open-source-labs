# Criar uma matriz aleatória

Em seguida, criaremos uma matriz aleatória usando numpy. Usaremos o método `rand` para criar uma matriz 5x3 com valores aleatórios entre 0 e 1. Também definiremos uma semente aleatória para garantir a reprodutibilidade dos resultados.

```python
# Fixing random state for reproducibility
np.random.seed(19680801)

X = 10*np.random.rand(5, 3)
```
