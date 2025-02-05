# Converting a Structured Array to a Record Array

We can convert a structured array to a record array using the `view` method and specifying the `np.recarray` type.

```python
# Convert a structured array to a record array
recordarr = x.view(np.recarray)
```
