# Gerando os Dados

Em seguida, geraremos alguns dados falsos para usar em nosso gráfico. Criaremos dois arrays, `a` e `b`, usando a função `arange` do NumPy. Em seguida, calculamos mais dois arrays, `c` e `d`, usando a função `exp` para computar a exponencial de `a` e `d` como o inverso de `c`.

```python
# Make some fake data.
a = b = np.arange(0, 3, .02)
c = np.exp(a)
d = c[::-1]
```
