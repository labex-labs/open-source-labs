# Generando los datos

A continuación, generaremos algunos datos falsos para usar en nuestra trama. Crearemos dos arrays, `a` y `b`, usando la función `arange` de NumPy. Luego calcularemos otros dos arrays, `c` y `d`, usando la función `exp` para calcular el exponencial de `a` y `d` como el inverso de `c`.

```python
# Make some fake data.
a = b = np.arange(0, 3,.02)
c = np.exp(a)
d = c[::-1]
```
