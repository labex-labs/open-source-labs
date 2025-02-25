# Elegir columnas

El argumento `usecols` se utiliza para seleccionar qué columnas importar. acepta un solo entero o una secuencia de enteros que corresponden a los índices de las columnas a importar.

```python
np.genfromtxt(StringIO(data), usecols=(0, -1))
```
