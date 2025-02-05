# Create the Subplots

We can create subplots using the `plt.subplot()` method. In this example, we will create three subplots with the first subplot taking up the first row and all three columns, and the second and third subplots taking up the second and third row, respectively, and sharing the x-axis with the first subplot.

```python
ax1 = plt.subplot(311)
ax2 = plt.subplot(312, sharex=ax1)
ax3 = plt.subplot(313, sharex=ax1, sharey=ax1)
```
