# Create Data

Next, we need to create some data to plot. In this example, we will create an array of values for time (`t`) and an array of values for voltage (`s`).

```python
t = np.arange(0.01, 5.0, 0.01)
s = np.exp(-t)
```
