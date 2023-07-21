# Creating the plot

We will create a plot using Matplotlib. We will create an instance `d` of the `DataDisplayDownsampler` class using xdata and ydata. We will create a figure and an axis using subplots function. We will hook up the line and set the autoscale on False. We will connect for changing the view limits, set the x limit and show the plot.

```python
d = DataDisplayDownsampler(xdata, ydata)
fig, ax = plt.subplots()
d.line, = ax.plot(xdata, ydata, 'o-')
ax.set_autoscale_on(False)
ax.callbacks.connect('xlim_changed', d.update)
ax.set_xlim(16, 365)
plt.show()
```
