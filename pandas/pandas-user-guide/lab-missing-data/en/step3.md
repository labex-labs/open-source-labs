# Insert Missing Data

Here, we'll see how to insert missing values into our data.

```python
# Insert missing values
s = pd.Series([1., 2., 3.])
s.loc[0] = None
```
