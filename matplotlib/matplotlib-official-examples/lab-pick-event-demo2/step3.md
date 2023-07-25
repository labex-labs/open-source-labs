# Plot the Data

Now, we will plot mu vs. sigma using Matplotlib's pyplot module. We will create a scatter plot using the computed values for mu and sigma. We will also add interactivity to the plot by setting the `picker` parameter to True.

```python
import matplotlib.pyplot as plt

fig, ax = plt.subplots()
ax.set_title('click on point to plot time series')
line, = ax.plot(xs, ys, 'o', picker=True, pickradius=5)
```
