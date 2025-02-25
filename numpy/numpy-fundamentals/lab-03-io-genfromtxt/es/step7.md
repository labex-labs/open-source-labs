# Usando valores faltantes y de relleno

Los argumentos `missing_values` y `filling_values` se utilizan para manejar datos faltantes. El argumento `missing_values` se utiliza para reconocer datos faltantes, y el argumento `filling_values` se utiliza para proporcionar un valor para las entradas faltantes.

```python
np.genfromtxt(StringIO(data), missing_values="N/A", filling_values=0)
```
