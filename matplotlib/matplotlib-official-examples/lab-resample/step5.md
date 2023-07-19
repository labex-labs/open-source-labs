# Creating the signal

We will create a signal using NumPy. We will create an array xdata using linspace function with start=16, stop=365 and num= (365-16)\*4. We will create an array ydata using sin and cos functions.

```python
xdata = np.linspace(16, 365, (365-16)*4)
ydata = np.sin(2*np.pi*xdata/153) + np.cos(2*np.pi*xdata/127)
```
