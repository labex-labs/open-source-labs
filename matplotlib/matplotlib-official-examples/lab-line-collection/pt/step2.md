# Criar Dados

Em seguida, precisamos criar os dados que usaremos para plotar as linhas. Usaremos `numpy` para criar um array 2D de valores `x` e `y`.

```python
x = np.arange(100)
ys = x[:50, np.newaxis] + x[np.newaxis, :]
```
