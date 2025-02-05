# Create Plots

In this step, we will create three plots using the masked array with different units.

```python
# create subplots
fig, (ax1, ax2, ax3) = plt.subplots(nrows=3, sharex=True)

# plot 1
ax1.scatter(xsecs, xsecs)
ax1.yaxis.set_units(secs)

# plot 2
ax2.scatter(xsecs, xsecs, yunits=hertz)

# plot 3
ax3.scatter(xsecs, xsecs, yunits=minutes)

# set labels
ax1.set_ylabel('Seconds')
ax2.set_ylabel('Hertz')
ax3.set_ylabel('Minutes')
ax3.set_xlabel('Time')
```
