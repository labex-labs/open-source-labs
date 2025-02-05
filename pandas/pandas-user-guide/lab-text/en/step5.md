# Create Dummy Variables

You can create dummy variables from string data using the `get_dummies` method.

```python
# create dummy variables
s = pd.Series(["a", "a|b", np.nan, "a|c"], dtype="string")
s.str.get_dummies(sep="|")
```
