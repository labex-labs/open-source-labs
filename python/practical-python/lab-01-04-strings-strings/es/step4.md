# Indexación de cadenas

Las cadenas funcionan como un array para acceder a los caracteres individuales. Se utiliza un índice entero, comenzando en 0. Los índices negativos especifican una posición relativa al final de la cadena.

```python
a = 'Hello world'
b = a[0]          # 'H'
c = a[4]          # 'o'
d = a[-1]         # 'd' (final de la cadena)
```

También se puede segmentar o seleccionar subcadenas especificando un rango de índices con `:`.

```python
d = a[:5]     # 'Hello'
e = a[6:]     # 'world'
f = a[3:8]    # 'lo wo'
g = a[-5:]    # 'world'
```

El carácter en el índice final no se incluye. Los índices faltantes asumen el principio o el final de la cadena.
