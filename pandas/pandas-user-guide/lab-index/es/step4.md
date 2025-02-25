# Trabajando con Datos Faltantes

Pandas proporciona varios métodos para limpiar datos y llenar valores faltantes.

```python
# Creando un DataFrame con valores faltantes
df = pd.DataFrame({'A': [1, 2, np.nan], 'B': [5, np.nan, np.nan], 'C': [1, 2, 3]})

# Llenando valores faltantes
df.fillna(value=0, inplace=True)
```
