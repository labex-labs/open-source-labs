# Define Data

Next, we need to define the data that we will use for our chart. We will create a sine wave with 201 data points:

```python
t = np.linspace(0.0, 2.0, 201)
s = np.sin(2 * np.pi * t)
```
