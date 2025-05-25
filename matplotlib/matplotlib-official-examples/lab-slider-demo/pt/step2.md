# Definir a Função da Onda Senoidal

Em seguida, definiremos a função que gerará nossa onda senoidal. A função receberá dois parâmetros, amplitude e frequência, e retornará a onda senoidal em um determinado tempo.

```python
def f(t, amplitude, frequency):
    return amplitude * np.sin(2 * np.pi * frequency * t)
```
