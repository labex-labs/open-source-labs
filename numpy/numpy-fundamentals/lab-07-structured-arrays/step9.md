# Converting a Record Array to a Structured Array

To convert a record array back to a structured array, we can use the `view` method and specify the original dtype of the structured array.

```python
# Convert a record array to a structured array
x = recordarr.view(dtype=[('name', 'U10'), ('age', int)])
```
