# Entendendo Atribuição Encadeada com CoW

Agora, vamos entender como a atribuição encadeada funciona com CoW.

```python
# Create a DataFrame
df = pd.DataFrame({"foo": [1, 2, 3], "bar": [4, 5, 6]})

# Apply chained assignment, which would violate CoW principles
df["foo"][df["bar"] > 5] = 100

# Print the DataFrame
print(df)
```
