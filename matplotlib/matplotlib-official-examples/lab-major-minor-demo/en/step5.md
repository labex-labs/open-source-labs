# Automatic tick selection for major and minor ticks

```python
# Create data
t = np.arange(0.0, 100.0, 0.01)
s = np.sin(2 * np.pi * t) * np.exp(-t * 0.01)

# Plot the data
fig, ax = plt.subplots()
ax.plot(t, s)

# Set the minor locator
ax.xaxis.set_minor_locator(AutoMinorLocator())

# Set the tick parameters
ax.tick_params(which='both', width=2)
ax.tick_params(which='major', length=7)
ax.tick_params(which='minor', length=4, color='r')

# Display the plot
plt.show()
```

In this step, we create new data and plot it. Then we set the minor locator to automatically select the number of minor ticks. After that, we set the tick parameters, i.e., the width and length of the ticks and their color, for both major and minor ticks. Finally, we display the plot.
