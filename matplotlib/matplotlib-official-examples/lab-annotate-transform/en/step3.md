# Create the Plot

Now, we will create the plot using the `matplotlib.pyplot` library. We will set the x and y limits of the plot and then plot the data.

```python
fig, ax = plt.subplots()
ax.plot(x, y)
ax.set_xlim(0, 10)
ax.set_ylim(-1, 1)
```
