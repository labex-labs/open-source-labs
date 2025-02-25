# Comprendiendo la Copia al Escribir con DataFrame

Ahora, creemos un DataFrame y veamos cómo la Copia al Escribir (CoW) afecta la modificación de datos.

```python
# Crea un DataFrame
df = pd.DataFrame({"foo": [1, 2, 3], "bar": [4, 5, 6]})

# Crea un subconjunto del DataFrame
subset = df["foo"]

# Modifica el subconjunto
subset.iloc[0] = 100

# Imprime el DataFrame original
print(df)
```

## Implementando la Copia al Escribir con DataFrame

Ahora, veamos cómo implementar la Copia al Escribir cuando se modifica un DataFrame.

```python
# Habilita la Copia al Escribir
pd.options.mode.copy_on_write = True

# Crea un subconjunto del DataFrame
subset = df["foo"]

# Modifica el subconjunto
subset.iloc[0] = 100

# Imprime el DataFrame original
print(df)
```
