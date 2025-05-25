# Verificando e Definindo a Flag de Rótulos Duplicados

Finalmente, podemos verificar e definir a flag `allows_duplicate_labels` em um DataFrame.

```python
# Criando um DataFrame e definindo allows_duplicate_labels como False
df = pd.DataFrame({"A": [0, 1, 2, 3]}, index=["x", "y", "X", "Y"]).set_flags(allows_duplicate_labels=False)

# Verificando a flag allows_duplicate_labels
print(df.flags.allows_duplicate_labels)

# Definindo allows_duplicate_labels como True
df2 = df.set_flags(allows_duplicate_labels=True)
print(df2.flags.allows_duplicate_labels)
```
