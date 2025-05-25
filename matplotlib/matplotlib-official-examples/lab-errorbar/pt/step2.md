# Criar dados de exemplo

Em seguida, criaremos dados de exemplo para usar no gráfico. Neste exemplo, usaremos a função `numpy.arange()` para criar um array de valores entre 0.1 e 4 com um passo de 0.5. Em seguida, usaremos a função `numpy.exp()` para calcular a exponencial de cada valor no array.

```python
# example data
x = np.arange(0.1, 4, 0.5)
y = np.exp(-x)
```
