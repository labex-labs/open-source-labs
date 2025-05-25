# Entendendo CoW com DataFrame

Agora, vamos criar um DataFrame e ver como o CoW afeta a modificação dos dados.

```python
# Create a DataFrame
df = pd.DataFrame({"foo": [1, 2, 3], "bar": [4, 5, 6]})

# Create a subset of the DataFrame
subset = df["foo"]

# Modify the subset
subset.iloc[0] = 100

# Print the original DataFrame
print(df)
```

## Implementando CoW com DataFrame

Agora, vamos ver como implementar o CoW ao modificar um DataFrame.

```python
# Enable CoW
pd.options.mode.copy_on_write = True

# Create a subset of the DataFrame
subset = df["foo"]

# Modify the subset
subset.iloc[0] = 100

# Print the original DataFrame
print(df)
```
