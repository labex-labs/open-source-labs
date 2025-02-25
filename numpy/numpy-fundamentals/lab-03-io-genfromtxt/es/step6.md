# Ajustando la conversión

El argumento `conversores` nos permite definir funciones de conversión para manejar conversiones más complejas. acepta un diccionario con índices de columna o nombres de columna como claves y funciones de conversión como valores.

```python
convertfunc = lambda x: float(x.strip(b"%"))/100.
np.genfromtxt(StringIO(data), conversores={1: convertfunc})
```
