# Dividiendo las líneas en columnas

El argumento `delimitador` se utiliza para definir cómo se deben dividir las líneas en columnas. Por defecto, `numpy.genfromtxt` asume `delimitador = None`, lo que significa que la línea se divide en blanco (incluyendo tabulaciones).

```python
np.genfromtxt(StringIO(data), delimitador=",")
```
