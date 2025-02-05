# Create the subfigures and call the `test_rotation_mode` function

We will create two subfigures and call the `test_rotation_mode` function with the `fig` and `mode` parameters.

```python
fig = plt.figure(figsize=(8, 5))
subfigs = fig.subfigures(1, 2)
test_rotation_mode(subfigs[0], "default")
test_rotation_mode(subfigs[1], "anchor")
plt.show()
```
