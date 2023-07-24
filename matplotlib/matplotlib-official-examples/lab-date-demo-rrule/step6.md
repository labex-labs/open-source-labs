# Plot the data and set the x-axis ticks

Finally, you can plot the data using the plot function, and set the x-axis ticks using the tick locator and formatter functions you set earlier.

```python
fig, ax = plt.subplots()
plt.plot(dates, s, 'o')
ax.xaxis.set_major_locator(loc)
ax.xaxis.set_major_formatter(formatter)
ax.xaxis.set_tick_params(rotation=30, labelsize=10)
plt.show()
```
