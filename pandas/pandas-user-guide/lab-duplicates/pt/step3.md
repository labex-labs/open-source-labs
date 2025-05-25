# Duplicatas na Indexação

Em seguida, veremos como duplicatas na indexação podem levar a resultados inesperados.

```python
# Criando um DataFrame com rótulos de coluna duplicados
df1 = pd.DataFrame([[0, 1, 2], [3, 4, 5]], columns=["A", "A", "B"])

# Indexando 'B' retorna uma Series
print(df1["B"])

# Indexando 'A' retorna um DataFrame
print(df1["A"])
```
