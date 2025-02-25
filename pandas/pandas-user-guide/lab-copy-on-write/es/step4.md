# Implementando la asignación encadenada con la Copia al Escribir

Finalmente, veamos cómo implementar la asignación encadenada con la Copia al Escribir (CoW) utilizando el método `loc`.

```python
# Crea un DataFrame
df = pd.DataFrame({"foo": [1, 2, 3], "bar": [4, 5, 6]})

# Aplica la asignación encadenada con CoW utilizando 'loc'
df.loc[df["bar"] > 5, "foo"] = 100

# Imprime el DataFrame
print(df)
```
