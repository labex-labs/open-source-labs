# Comprobando la eficiencia de la memoria

A continuación, comprobaremos la eficiencia de la memoria al utilizar estructuras de datos dispersas. Crearemos un gran DataFrame, lo convertiremos en disperso y luego compararemos el uso de memoria.

```python
# Creando un gran DataFrame con valores aleatorios
df = pd.DataFrame(np.random.randn(10000, 4))

# Estableciendo la mayoría del DataFrame en NaN
df.iloc[:9998] = np.nan

# Convirtiendo el DataFrame en disperso
sdf = df.astype(pd.SparseDtype("float", np.nan))

# Comprobando el uso de memoria del DataFrame denso vs disperso
print('denso : {:0.2f} bytes'.format(df.memory_usage().sum() / 1e3))
print('disperso: {:0.2f} bytes'.format(sdf.memory_usage().sum() / 1e3))
```
