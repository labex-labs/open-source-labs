# Understanding CoW with DataFrame

Now, let's create a DataFrame and see how CoW affects the modification of data.

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

## Implementing CoW with DataFrame

Now, let's see how to implement CoW when modifying a DataFrame.

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
