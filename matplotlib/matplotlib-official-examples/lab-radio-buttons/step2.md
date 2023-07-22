# Create Data

Next, we will create the data that will be used in the plot. We will create three different sine waves with different frequencies using the `numpy` library.

```python
t = np.arange(0.0, 2.0, 0.01)
s0 = np.sin(2*np.pi*t)
s1 = np.sin(4*np.pi*t)
s2 = np.sin(8*np.pi*t)
```
