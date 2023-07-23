# Implementing Chained Assignment with CoW

Finally, let's see how to implement chained assignment with CoW using the `loc` method.

```python
# Create a DataFrame
df = pd.DataFrame({"foo": [1, 2, 3], "bar": [4, 5, 6]})

# Apply chained assignment with CoW using 'loc'
df.loc[df["bar"] > 5, "foo"] = 100

# Print the DataFrame
print(df)
```
