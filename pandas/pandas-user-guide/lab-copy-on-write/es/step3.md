# Comprendiendo la asignación encadenada con la Copia al Escribir

Ahora, veamos cómo funciona la asignación encadenada con la Copia al Escribir (CoW).

```python
# Crea un DataFrame
df = pd.DataFrame({"foo": [1, 2, 3], "bar": [4, 5, 6]})

# Aplica la asignación encadenada, lo que violaría los principios de la Copia al Escribir
df["foo"][df["bar"] > 5] = 100

# Imprime el DataFrame
print(df)
```
