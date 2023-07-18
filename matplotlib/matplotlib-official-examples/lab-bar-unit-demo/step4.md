# Define the Bar Chart Parameters

The next step is to define the parameters for the bar chart. We will define the x locations for the groups, the width of the bars, and the labels for the x-ticks.

```python
ind = np.arange(N)    # the x locations for the groups
width = 0.35         # the width of the bars
ax.set_xticks(ind + width / 2, labels=['G1', 'G2', 'G3', 'G4', 'G5'])
```
