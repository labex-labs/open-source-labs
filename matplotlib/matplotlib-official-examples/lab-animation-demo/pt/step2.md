# Gerar dados aleatórios

Geraremos um array 3D de dados aleatórios usando `numpy.random.random()`. Usaremos um valor de semente (seed) para garantir que o mesmo conjunto de dados seja gerado cada vez que o código for executado.

```python
np.random.seed(19680801)
data = np.random.random((50, 50, 50))
```
