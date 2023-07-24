# Create Data for the Plots

We need to create data for the plots to visualize. In this example, we will create three different datasets using NumPy.

```python
t = np.arange(0.01, 5.0, 0.01)
s1 = np.sin(2 * np.pi * t)
s2 = np.exp(-t)
s3 = np.sin(4 * np.pi * t)
```
