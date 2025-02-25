# Comprobando y configurando la bandera de etiquetas duplicadas

Finalmente, podemos comprobar y configurar la bandera `allows_duplicate_labels` en un DataFrame.

```python
# Creando un DataFrame y configurando allows_duplicate_labels en False
df = pd.DataFrame({"A": [0, 1, 2, 3]}, index=["x", "y", "X", "Y"]).set_flags(allows_duplicate_labels=False)

# Comprobando la bandera allows_duplicate_labels
print(df.flags.allows_duplicate_labels)

# Configurando allows_duplicate_labels en True
df2 = df.set_flags(allows_duplicate_labels=True)
print(df2.flags.allows_duplicate_labels)
```
