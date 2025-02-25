# Crear datos

En este paso, crearemos un diccionario `data` que contiene valores para las variables `a`, `b`, `c` y `d`.

```python
data = {'a': np.arange(50),
        'c': np.random.randint(0, 50, 50),
        'd': np.random.randn(50)}

data['b'] = data['a'] + 10 * np.random.randn(50)
data['d'] = np.abs(data['d']) * 100
```
