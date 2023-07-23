# Create Data

In this step, we will create the data for our error bar plot. We will use NumPy to create an array of theta values and an array of corresponding radius values.

```python
theta = np.arange(0, 2 * np.pi, np.pi / 4)
r = theta / np.pi / 2 + 0.5
```
