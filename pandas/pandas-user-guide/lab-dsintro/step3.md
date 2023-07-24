# Creating a DataFrame

The other fundamental data structure is the DataFrame. It's a two-dimensional labeled data structure with columns of potentially different types.

```python
# Create a DataFrame
df = pd.DataFrame(np.random.randn(6, 4), columns=list('ABCD'))
```
