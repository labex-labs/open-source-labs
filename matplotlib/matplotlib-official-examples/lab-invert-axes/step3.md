# Create the Plot

Now, we can create the plot using Matplotlib. We will use the `plot` function to plot our data and set the limits of the x-axis using the `set_xlim` function.

```python
fig, ax = plt.subplots()

ax.plot(t, s)
ax.set_xlim(5, 0)  # decreasing time
ax.set_xlabel('decreasing time (s)')
ax.set_ylabel('voltage (mV)')
ax.set_title('Should be growing...')
ax.grid(True)

plt.show()
```
