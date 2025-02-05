# Create Data

Next, we will create some data to plot. We will be using the `numpy` library to create a sine wave.

```python
x = np.arange(0, 10, 0.005)
y = np.exp(-x/2.) * np.sin(2*np.pi*x)
```
