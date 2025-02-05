# Creating a figure and setting the background

We will create a figure using the `plt.figure()` method, which creates a `matplotlib.figure.Figure` instance. We will set the background color of the figure using the `rect.set_facecolor()` method.

```python
fig = plt.figure()
rect = fig.patch  # a rectangle instance
rect.set_facecolor('lightgoldenrodyellow')
```
