# Create Data Points

In this step, we will create some data points using the custom unit class - `Foo`.

```python
# create some Foos
x = [Foo(val, 1.0) for val in range(0, 50, 2)]
# and some arbitrary y data
y = [i for i in range(len(x))]
```
