# Gerar Dados

Geramos alguns dados de amostra para plotar, usando a função `mgrid` do `numpy`.

```python
# setup some generic data
N = 37
x, y = np.mgrid[:N, :N]
Z = (np.cos(x*0.2) + np.sin(y*0.3))
```
